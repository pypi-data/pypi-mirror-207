"""
Hilly
"""
from importlib import metadata
from typing import Tuple

from . import io, ski

__version__ = metadata.version(__package__ or __name__)

del metadata


def process_ski(filename: str, output: str) -> Tuple[io.gpd.GeoDataFrame, dict]:
    """Process a single ski day's GPX trace, print a summary, and output to GPKG."""

    df = io.load_trace(filename)
    df = ski.apply_filters(df)
    ski_summary = ski.summary(df)
    io.save_trace(df, output)

    return (df, ski_summary)
