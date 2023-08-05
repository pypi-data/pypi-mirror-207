"""

General utilities

"""
from typing import Tuple

import geopandas as gpd
import matplotlib as mpl
import numpy as np
import pyproj
from loguru import logger
from scipy.interpolate import splev, splprep
from scipy.ndimage import gaussian_filter
from shapely.geometry import LineString, Point, Polygon, box
from shapely.ops import transform

from . import constants


def transform_polygon(polygon: Polygon, in_crs: str, out_crs: str) -> Polygon:
    """Reproject a shapely polygon."""
    project = pyproj.Transformer.from_crs(
        pyproj.CRS(in_crs),
        pyproj.CRS(out_crs),
        always_xy=True,
    ).transform
    return transform(project, polygon)


def _line_fit_goodness(x, y) -> float:
    """Fit line and report how good it is."""
    res = np.polyfit(x, y, deg=1, full=True)
    return res[1][0]


def get_angle(p1: Point, p2: Point, p3: Point) -> float:
    """Get the positive angle between two lines segments."""
    v1 = np.array([p1.x, p1.y]) - np.array([p2.x, p2.y])
    v2 = np.array([p3.x, p3.y]) - np.array([p2.x, p2.y])
    norms = np.linalg.norm(v1) * np.linalg.norm(v2)
    dot = np.abs(np.dot(v1, v2.T))
    if norms < 10e-8 or dot < 10e-8 or (norms - dot) < 10e-8:
        return 0.0
    else:
        return np.arccos(dot / norms)


def smooth(x, window_len=11, window="hanning"):
    """smooth the data using a window with requested size.

    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.

    input:
        x: the input signal
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.

    output:
        the smoothed signal

    example:

    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)

    see also:

    np.hanning, np.hamming, np.bartlett, np.blackman, np.convolve
    scipy.signal.lfilter

    TODO: the window parameter could be the window itself if an array instead of a string
    """

    s = np.r_[x[window_len - 1 : 0 : -1], x, x[-2 : -window_len - 1 : -1]]

    if window == "flat":
        w = np.ones(window_len, "d")
    else:
        w = eval("np." + window + "(window_len)")

    y = np.convolve(w / w.sum(), s, mode="valid")

    return y[(window_len // 2 - 1) : -(window_len // 2 + (window_len % 2))]


def get_distance(pts: gpd.GeoSeries, english=False) -> float:
    """Convert the input GeoSeries to a LineString and compute the distance."""
    d = LineString(pts).length
    if english:
        return constants.METERS_TO_MILES * d
    else:
        return d


def rasterize(
    df: gpd.GeoDataFrame,
    method: str = "density",
    res: int = 10,
    runs_only: bool = False,
    run_column: str = "labels_str",
    smooth: bool = True,
) -> Tuple[np.ndarray, Tuple[float, float, float, float]]:
    """
    Rasterize the Point Geometries in the input dataframe according to the method. Ski runs
    are interploated and resampled for cleaner looking results.

    Note:
    Methods included are:
      * total: sum of points within pixel
      * density: sum of point within pixel divided by the overall max.
    Run options, runs_only and run_column, are for ski traces passed through tracetoosl.ski.apply_filters.
    """

    left, bottom, right, top = df.buffer(res * 2).unary_union.bounds
    # round bounds to resolution
    left_r = int(np.floor(left // res) * res)
    bottom_r = int(np.floor(bottom // res) * res)
    right_r = res + int(np.floor(right // res) * res)
    top_r = res + int(np.floor(top // res) * res)

    bounds = (left_r, bottom_r, right_r, top_r)

    width = (right_r - left_r) // res
    height = (top_r - bottom_r) // res

    if runs_only:
        logger.info("only including runs in rasterization.")
        indx_xs = []
        indx_ys = []
        for i in df[run_column].unique():
            if "run-" in i:
                indx_xs.append(np.floor((df[df[run_column] == i].geometry.x - left) / res).astype(int))
                indx_ys.append(np.floor((top - df[df[run_column] == i].geometry.y) / res).astype(int))
        indx_x = np.concatenate(indx_xs)
        indx_y = np.concatenate(indx_ys)
    else:
        # get the array index for each point
        indx_x = np.floor((df.geometry.x - left) / res).astype(int)
        indx_y = np.floor((top - df.geometry.y) / res).astype(int)

    # create array
    arr = np.zeros((height, width))
    for i, j in zip(indx_y, indx_x):
        arr[i, j] += 1

    if method == "total":
        pass
    elif method == "density":
        arr = arr / arr.max()
    else:
        raise ValueError(f"unknown method: {method}.")

    if smooth:
        arr = gaussian_filter(arr, sigma=5)

    return (arr, bounds)


def resample(x: np.array, y: np.array) -> np.array:
    """Fit spline to points and resample"""
    tck, u = splprep([x, y], s=0)
    new_points = splev(u, tck)
    return new_points


def colorize(array, cmap="viridis"):
    normed_data = (array - array.min()) / (array.max() - array.min())
    cm = mpl.colormaps[cmap]
    return cm(normed_data)
