"""
Working with Skiing/Snowboarding GPS Traces
"""
import geopandas as gpd
import numpy as np
import pandas as pd

from . import utils


def label_segments(df: gpd.GeoDataFrame) -> np.ndarray:
    """Label lifts as negative counts and runs as positive counts."""

    # use the time segments between stops to determine if we were on a lift or run
    prev_stopped = df.stopped.iloc[0]
    labels = np.zeros(df.shape[0])
    prev_segment = None
    lift_count = -1
    ride_count = 1
    for i, row in df.iterrows():
        curr_stopped = row["stopped"]

        if prev_stopped != curr_stopped:
            if prev_stopped and not curr_stopped:
                start = row["seconds"]
                start_z = row["z_smooth"]
            elif not prev_stopped and curr_stopped:
                stop = row["seconds"]
                stop_z = row["z_smooth"]
                diff_z = stop_z - start_z
                if np.abs(diff_z) > 20:
                    if diff_z > 0:
                        labels[(df.seconds > start) & (df.seconds < stop)] = lift_count
                        if prev_segment is not None and prev_segment == "ride":
                            lift_count -= 1
                        prev_segment = "lift"
                    elif diff_z < 0:
                        labels[(df.seconds > start) & (df.seconds < stop)] = ride_count
                        if prev_segment is not None and prev_segment == "lift":
                            ride_count += 1
                        prev_segment = "ride"
        prev_stopped = curr_stopped

    return labels


def apply_filters(
    df: gpd.GeoDataFrame,
    smooth_win: int = 30,
    dx_min: float = 2.0,
    dy_min: float = 2.0,
    dz_min=0.5,
) -> gpd.GeoDataFrame:
    """Apply smoothing, filtering, and add features that are useful for skiing analysis."""

    df["x"] = df.geometry.x
    df["y"] = df.geometry.y
    df["x_smooth"] = utils.smooth(df.x, smooth_win)
    df["y_smooth"] = utils.smooth(df.y, smooth_win)
    df["z_smooth"] = utils.smooth(df.ele, smooth_win)
    df["dx"] = np.gradient(df.x_smooth)
    df["dy"] = np.gradient(df.y_smooth)
    df["dz"] = np.gradient(df.z_smooth)
    df["speed_smooth"] = utils.smooth(df.speed, smooth_win)

    # stopped when horizontal change is low or vertical change is low
    df["stopped"] = np.logical_or(
        np.logical_and(np.abs(df.dx) < dx_min, np.abs(df.dy) < dx_min), np.abs(df.dz) < dz_min
    )

    # identify lifts/runs
    df["labels"] = label_segments(df)

    # mark as strings too
    df["labels_str"] = ""
    df.loc[df.labels > 0, "labels_str"] = df[df.labels > 0].apply(lambda r: f"run-{int(r['labels'])}", axis=1)
    df.loc[df.labels < 0, "labels_str"] = df[df.labels < 0].apply(lambda r: f"lift{int(r['labels'])}", axis=1)

    return df


def summary(df: gpd.GeoDataFrame) -> dict:
    """Prints a summary of the ski day."""

    runs = int(df.labels.max())
    lifts = int(df.labels.min())
    total_dist = 0
    longest_run = -1
    total_ride_time = pd.Timedelta(0)
    total_lift_time = pd.Timedelta(0)
    dists = {}
    summary_dict = {}
    for r in range(lifts, runs + 1):
        time_range = df[df.labels == r].time.max() - df[df.labels == r].time.min()
        if r > 0:
            d = utils.get_distance(df[df.labels == r].geometry)
            dists[r] = d
            total_dist += d
            if d > longest_run:
                longest_run = d
            total_ride_time += time_range
        elif r < 0:
            total_lift_time += time_range

    ride_ratio = total_ride_time / total_lift_time

    print("🏂 Ski Stats ⛷")
    print(f"    runs: {runs}")
    print(f"    Total Dist(km): {total_dist / 10**3}")
    print(f"    Longest Run(km): {longest_run / 10**3}")
    print(f"    Total time: {total_ride_time}")
    print(f"    Total lift time: {total_lift_time}")
    print(f"    Time Ratio: {ride_ratio}")

    summary_dict["runs"] = int(runs)
    summary_dict["total_dist"] = total_dist
    summary_dict["longest_run"] = longest_run
    summary_dict["total_ride_time"] = total_ride_time
    summary_dict["total_lift_time"] = total_lift_time
    summary_dict["ride_ratio"] = ride_ratio

    return summary_dict
