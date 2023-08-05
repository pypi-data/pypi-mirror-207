
<p align="center">
  <img src="docs/img/hilly-icon_sm.png" />
</p>


# Hilly

Tools for summarizing and viewing sporty GPX traces

## Install

```bash
pip install hilly
```

## Dev Install

```
git clone
cd hilly
poetry install
```

## Features

  * Traces are loaded as GeoDataFrames (convenient exploring and editing)
  * Rasterize traces to see popular routes/trails.
  * Label/Filter Skiing Trace to label/exclude chair-lifts.
  * Summary for Skiing day

## Usage

Import a trace:

```python
import hilly

df = hilly.io.load_trace("path/to/trace.gpx")
```

If it is a ski/snowboarding trace, apply filters to identify runs/lifts:

```python
ski_df = hilly.ski.apply_filters(df)
ski_df.labels_str.unique().tolist()
# ['', 'lift-1', 'run-1', 'run-2', 'lift-2', 'run-3', 'lift-3', 'run-4']
```

The `labels_str` column labels points in the trace as belonging to a lift ride or run, otherwise it is empty. The number indicates a count of lift/runs.

From there you can get a summary for the trace (assuming it is over a single day):

```python
summary = hilly.ski.summary(ski_df)
#🏂 Ski Stats ⛷
#    runs: 4
#    Total Dist(km): 4.815023209198009
#    Longest Run(km): 1.409849302232853
#    Total time: 0 days 00:17:32
#    Total lift time: 0 days 00:36:55.990000
#    Time Ratio: 0.4747313841668961
```

Or, you can view the trace:

```python
# open leaflet map showing points, dropping datetime column for proper JSON
m = ski_df.drop(columns=["time"]).explore("labels", cmap="coolwarm_r")
m.show_in_browser()
```
![ski-point-map](docs/img/ski-point-map.png)

or rasterize the trace to get a density map:
```python
arr, bounds = hilly.utils.rasterize(ski_df, runs_only=True, res=1)
m = hilly.io.map_raster(arr, bounds)
m.show_in_browser()
```
![ski-raster-map](docs/img/ski-raster-map.png)

# Collecting Traces

There are many apps available for collecting traces. I use [OpenTracks](https://opentracksapp.com/) and follow the Export instructions from the settings menu.
