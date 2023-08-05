"""
General IO for GPS Traces
"""
from typing import Optional, Tuple

import folium
import geopandas as gpd
import gpxcsv
import numpy as np
import numpy.ma as ma
import pandas as pd
import rasterio
from shapely.geometry import Point, Polygon, box

from . import constants, utils


def load_trace(
    filename: str,
    time_clip: Tuple[pd.Timestamp, pd.Timestamp] = (),
    geo_clip: Optional[Polygon] = None,
    fill_nans: bool = True,
    out_srs: str = constants.SRS,
) -> gpd.GeoDataFrame:
    """
    Load a GPS trace from a GPX file, optionally provide
    clipping time-range or geo-range (shapely polygon in WGS84).

    Note:
    Defaults to reprojecting geometries to EASE Grid 2.0.
    """

    df = pd.DataFrame(gpxcsv.gpxtolist(filename))
    df.time = pd.to_datetime(df.time)
    df["time_int"] = df.time.apply(lambda t: t.timestamp())
    df["seconds"] = df.time_int - df.time_int[0]
    df["geometry"] = df.apply(lambda r: Point(r["lon"], r["lat"]), axis=1)
    gdf = gpd.GeoDataFrame(df, crs="EPSG:4326")

    if time_clip:
        start, stop = time_clip
        gdf = gdf[(gdf.time > start) & (gdf.time < stop)]

    if geo_clip is not None:
        gdf = gdf[gdf.within(geo_clip)]

    if fill_nans:
        gdf.loc[np.isnan(gdf.speed), "speed"] = 0.0

    return gdf.to_crs(out_srs)


def save_trace(df: gpd.GeoDataFrame, output: str) -> None:
    """Save a trace to a file."""
    df.to_file(output)


def save_raster(
    arr: np.ndarray,
    bounds: Tuple[float, float, float, float],
    res: int,
    output: str,
    out_srs: str = constants.SRS,
) -> None:
    """Write summary array to a GeoTiff."""

    profile = dict(
        driver="GTiff",
        height=arr.shape[0],
        width=arr.shape[1],
        count=1,
        dtype=arr.dtype,
        crs=out_srs,
        nodata=0,
        transform=rasterio.transform.from_bounds(*bounds, width=arr.shape[1], height=arr.shape[0]),
    )

    with rasterio.open(output, "w", **profile) as ds:
        ds.write(arr, 1)


def map_raster(
    arr: np.array,
    bounds: Tuple[float, float, float, float],
    clip: str = "percentile",
    cmap="Blues",
    in_srs: str = constants.SRS,
) -> None:
    """Create a leaflet map with folium for an input raster."""

    arr = np.flipud(arr)

    # need bounds in WGS83
    wgs_poly = utils.transform_polygon(box(*bounds), in_srs, "EPSG:4326")
    left, bottom, right, top = wgs_poly.bounds
    center_y = (right + left) / 2.0
    center_x = (top + bottom) / 2.0

    m = folium.Map([center_x, center_y], zoom_start=13)

    # clip the arr?
    if clip == "percentile":
        a_min = np.percentile(arr, 2)
        a_max = np.percentile(arr, 98)
        arr = np.clip(arr, a_min, a_max)

    arr[arr == 0.0] = np.nan

    arr_c = utils.colorize(ma.masked_invalid(arr), cmap)

    folium.raster_layers.ImageOverlay(
        image=arr_c,
        bounds=[[bottom, left], [top, right]],
        origin="lower",
        opacity=0.7,
        mercator_project=True,
    ).add_to(m)

    return m
