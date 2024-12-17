# climate_data_integration

This repository contains Ana Uribe and Nithya Murikinati's final project code and documentation for CSCI 8735: Advanced Database Systems (Fall 2024).

## Introduction

We hope to create a Python-based software to help integrate climate science data.

**Motivation:** Climate data is collected by different organizations ([NASA](https://science.nasa.gov/earth/), [ECMWF](https://www.ecmwf.int), etc.)and instruments ([ARIS](https://airs.jpl.nasa.gov), [MODIS](https://modis.gsfc.nasa.gov/about/)), so multiple entities could collect for a given spatial ($S$) and temporal range ($T$):
* The exact same data at the same time and location within $S$ and $T$.
* The exact same data at different time intervals and/or different locations within $S$ and $T$.
* Similar or related data at the same or different time and location within $S$ and $T$.

Unifying these various datasets can help scientists analyze the region $S$ or time range $T$ of interest with all the available data. Many climate scientists are using various datasets, or 'multi-source' data, to answer specific questions or for training models to predict things like weather or sea-level temperature. A pipeline that can do this integration will help streamline this process. Our project will focus on integration between files, which is one aspect of this pipeline.

<!-- Thus, given several datasets, our software will return integrated (unified) data and corresponding metadata. -->
Thus, given a set of files, our project will find the data that overlaps in time and space, consolidate it, and return the updated files. Additionally, it will provide some metadata describing the integration process. We assume the set of files are of the same file type and the same spatial and temporal range and intervals (i.e., values are sampled in the same location at the same time).

**Project Contributions:**

* File integration: column-matching, aggregation, deletion, statistics.
* Integration metadata: information about deduplicated data such as the amount of duplicates found, the columns that were merged or deleted etc.

Below we describe the pipeline our project will fit into. The first 4 points are out of the scope of our work but important to understand as given in the process, while the last 3 points are what we are implementing.

**Data Integration Pipeline:** 

<!-- The following steps outline our plan to integrate various datasets in a comprehensive way. -->
1. *Unify Data Format*: Data coming from various sources must be of the same file type for easier integration. For our project, we assume all the data formats are the same.
2. *Variable Matching*: Data columns in different datasets may have different names for the same variable (such as "temp", "temperature", "Temp", etc.). Our project will check and unify these columns. However, we will assume we will not encounter an unexpected variable, meaning all the column names we encounter are accounted for in our variable matching code.
3. *Grid Data*: Different datasets may project onto the Earth using a different grid or projection. Re-gridding all the data to the same projection (if possible), is important to do before deduplication. However, [PostGIS](https://postgis.net/docs/ST_Transform.html) is an established tool that accomplishes this and is used by many databases, and so we will assume all data is gridded to the common grid: [WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84).
4. *Consolidate Temporal Resolution*: Similar to regridding the data, datapoints may be taken at varying intervals (e.g., daily versus hourly intervals, or monthly intervals at different days of the month). A data integration pipeline should determine how to merge or consolidate these points, or develop a way to keep all the information with varying time intervals between points. Our project assumes the temporal resolution is the same for all data files.
5. **Find Duplicates**: Our project will find duplicate data within the same or different files.
6. **Manage Duplicates**: Our project will provide various ways to handle duplicate data such as aggregating, deleting, and calculating statistics about measurements.
7. **Provide Metadata**: For deduplicated data, provide information about what data was deduplicated, deduplication methods, etc..

<!-- 0. *Best Practices:* Look into the climate science literature and determine the most common data format, grid, time range, variables, etc.. This will help us decide the framework to unify all datasets to. Thus, all the steps below are subject to change due to current best practices.
1. *Unify Data Format:* The first thing to do will be to convert all incoming data to the same format.
2. *Variable Matching:* Incoming datasets may have different names for the same variables (such as "temp." for "temperature" etc.), so starting with a set of expected values, we will have a process that checks all the columns of incoming datasets and “column-matches” the values or adds a new value to the set if there is a new value.
3. *Grid Data:* While some data is already [gridded](https://climateestimate.net/content/gridded-data.html#:~:text=These%20generally%20consist%20of%20combining,at%20each%20gridpoint%20and%20timestep.) (divided into latitude x longitude grid over the surface area of the Earth), data may use different grids, so all the data must be re-gridded to the same grid. Other data is not gridded, so it must be gridded or stored separately such that it is easy to use gridded and non-gridded data together.
4. *Consolidate Temporal Resolution:* Datapoints may be taken at varying time intervals. Here we determine what to do when points coincide, and when they don't. This could include merging data points, deleting redundant data, or developing a way to keep all the information with varying time intervals between points.
5. *Find Duplicates:* Some records may hold the same measurement for the same variable. If the value is exactly the same, we can just keep one. If the values are not the same, we can calculate some statistics about the measurement to give a more accurate idea to scientists regarding the range of this value.
6. *Manage Duplicates:* Provide various ways to handle duplicate data such as aggregating, deleting, etc..
7. *Join Similar Data:* Data may not be the same but may be useful to have together, such as the u component of the wind and the v component of the wind.
8. *Provide Metadata:* For the integrated data, provide useful metadata that keeps track of where data came from, the extent of information, aggregation methods, etc.. -->

---
Below are some resources and notes about each process of the pipeline that helped us find our project scope.

<!-- Below are the descriptions of the current best practices in the climate/earth science research community for the varying steps of the pipeline. -->

## General Resources

The following resources discuss the physical sciences of climate science. This will be useful to get a general idea of the data that is necessary and useful for climate scientists.

* Intergovernmental Panel on Climate Change Sixth Assesment [Report](https://www.ipcc.ch/report/ar6/wg1/) gives an overview of the science driving climate change.
* Encyclopedia of Earth Weather and Climate [Tab](https://editors.eol.org/eoearth/wiki/Weather_%26_Climate) defines various aspects of the weather and climate.

The following resources are to get an idea of the best practices of each part of the integration and deduplication pipeline.

* Practical Guide to Climate Econometrics [Introduction](https://climateestimate.net/content/getting-started.html) gives a good introduction into finding and using weather data, common file formats in the field, etc..
* The Spatio-Temporal-Access-Catalog [Index](https://stacspec.org/en) is a specification that provides an API, datasets, etc. that allows data to be handled which we can look at for an example of how to code our software.
* The odc-stac python function [documentation](https://odc-stac.readthedocs.io/en/latest/intro.html) gives an example of an existing python software that helps analyze Sentinel 2 [data](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-2).
* Learning the Earth with Artificial Intelligence and Physics [LEAP](https://leap.columbia.edu) is an NSF science and technology center for integrating physical models and machine learning for climate science. Its documentation may help us to determine how data is best integrated for use in ML, climate science, and data science.
* Earthaccess python [library](https://www.earthdata.nasa.gov/news/blog/earthaccess-earth-science-data-simplified) is NASA's python library for helping users work with their data, which is the type of data we are interested in integrating with others.
* U.S. Antarctic Program Data [Center]() documents, preserves, and disseminates data from Antarctica, which can be a good example for us in terms of documentation.

## Unifying Format
**Common Data Formats:**
* netcdf
* Json
* csv

**Final Data Format:**
netcdf

## Variable Matching
**Expected Variables Set from Intergovernmental Panel on Climate Change Sixth Assesment:** 
* Carbon dioxide ($CO_2$)
* Methane ($CH_4$)
* Nitrous oxide ($N_2O$)
* Mean surface temperature
* Snow cover
* Well-mixed greenhouse gasses
* Wind speed
* Permafrost
* Snowfall
* Hail
* Halogeneated gasses
* Volatile organic compounds and carbon monoxide
* Sulphur dioxide ($SO_2$)
* Organic compound
* Amonia
* Black carbon
* Percipitation
* Moisture level
* Surface level humidity
* Land-use reflectance and irrigation
* Aviation contrails
* Costal flood
* Infrared energy emitted from earth surface
* Spectral bands/wavelenthds
* Ocean acidity
* Ocean salinity
* Ice sheet mass
* Ocean oxygen levels
* Relativesea level
* Surface open ocean pH


## Grid Data
A Spatial Reference System Identifier ([SRID](https://en.wikipedia.org/wiki/Spatial_reference_system#Identifier)) is used to specify the projection or lack of projection of geographical spatial data.

Spatial data providers either create their own projection, or use official projections from the European Petroleum Survey Group ([EPSG](https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset)) or the Environmental Systems Research Institute ([Esri](https://en.wikipedia.org/wiki/Esri)).

These projections define the coordinate system, and thus, data must be converted into the same grid in order to be used together.

**Final Grid:**
While there are many grids to choose from, one with high accuracy (up to 1 meter for the whole world) is a common one we will convert our data to. This grid has the SRID [WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84) and is used by the Global Positioning System. Additional [reference](https://epsg.io/6933).

**Tools:**
[PostGIS](https://postgis.net/docs/ST_Transform.html) Provides a way to transform data from one grid to another. Other databases like [Snowflake](https://docs.snowflake.com/en/sql-reference/functions/st_transform) use this feature to work with their spatial data.

## Temporal Resolution
**Possible Temporal Resolutions:** Minutes, Hourly, Daily, Monthly, Yearly, 

## Data Deduplication
**Current Practice:**

## Data Joining
**Data to store together:**
* U component of wind, V component of wind as tuple: `[u, v]`

## Dataset Metadata

## Data Documentation

<!-- There is a lot of different data repositories available that we can use to get data and show our integration methods. There are also different types of datasets, some of which generate the others, and thus should not be "re-aggregated". Thus, we will have to determine what to do when "combining/unifying/integrating" these different types of datasets. -->
There are a lot of different climate data repositories. Below is a general overview of the climate science data landscape, and then the specific data we used to test our deduplication methods.

### Data Repositories List

* [NOAA](https://psl.noaa.gov/data/gridded/)
* [CDS](https://cds.climate.copernicus.eu)
* [AMRDC](https://amrdcdata.ssec.wisc.edu)
* [Artic Data Center](https://arcticdata.io)
* [ESDS](https://earthdata.nasa.gov_)
* [SENTINEL](https://sentinels.copernicus.eu/web/sentinel/home)

### Types of Datasets

* Analysis (data in database from sources)
* Reanalysis (weather observations + computer model = global weather)
* Forecast (historical data → future predictions)
* Reforecast (reanalysis → “future” predictions)
* Climate simulation (science + factors = scenarios)

### Data Used
**Met Office Hadley Centre Sea Ice and Sea Surface Temperature dataset**
Information
* Meteorological Office (UK)
* Time range: 1850 - 2024
* Temporal resolution: monthly
* Spatial range: global
* Spatial resolution: 1.0 degree x 1.0 degree gridded

Titchner, H. A., and N. A. Rayner (2014), The Met Office Hadley Centre sea ice and sea surface temperature data set, version 2: 1. Sea ice concentrations, J. Geophys. Res. Atmos., 119, 2864-2889, doi: 10.1002/2013JD020316. Version HadISST.2.2.0.0, Download: 2.12

**COBE-SST 2 and Sea Ice data**
Information
* National Oceanic and Atmospheric Administration (USA)
* Time range: 1850 - 2024
* Temporal resolution: monthly
* Spatial range: global
* Spatial resolution: 1.0 degree x 1.0 degree gridded

COBE-SST 2 and Sea Ice data provided by the NOAA PSL, Boulder, Colorado, USA, from their website at https://psl.noaa.gov

## Repository Layout

Note this repository is set up to hold the full data integration pipeline, so not all the files will be filled for this project. The files that are used for this project have a `<-- PROJECT` to the right of the file name and description.

    project-root/
    ├── data/                         <-- PROJECT
    │   ├── raw/                      # Store raw incoming data files
    │   ├── processed/                # Store processed data files
    │   └── metadata/                 # Store metadata files
    ├── src/
    │   ├── pipeline.py               # Main pipeline function
    │   ├── unify_format.py           # Step 1 function of Data Pipeline
    │   ├── variable_matching.py      # Step 2 function      <-- PROJECT
    │   ├── regrid.py                 # Step 3 function
    │   ├── temporal_resolution.py    # Step 4 function
    │   ├── deduplicate.py            # Step 5 & 6 function  <-- PROJECT
    │   ├── data_joining.py           # Step 7 function      <-- PROJECT
    │   ├── metadata_generator.py     # Step 8 function      <-- PROJECT
    │   └── utils.py                  # Common utilities     <-- PROJECT
    ├── notebooks/                    # Jupyter notebooks for testing and visualization
    ├── tests/
    │   ├── test_unify_format.py        
    │   ├── test_variable_matching.py               <-- PROJECT
    │   ├── test_regrid.py
    │   ├── test_temporal_resolution.py
    │   ├── test_deduplicate.py                     <-- PROJECT
    │   ├── test_data_joining.py                    <-- PROJECT
    │   └── test_metadata_generator.py              <-- PROJECT
    ├── scripts/
    |   ├── deduplicate_data.py       # Script to run the data deduplication        <-- PROJECT
    │   ├── integrate_data.py         # Script to run the full data integration pipeline
    │   ├── preprocess_data.sh        # Example shell script for data processing
    │   └── analyze_output.sh         # Example script for analyzing outputs        <-- PROJECT
    ├── requirements.txt              # Dependencies      <-- PROJECT
    ├── README.md                     # Overview of the project         <-- PROJECT
    └── .gitignore      <-- PROJECT

<!-- └── .github/
        ├── workflows/
        │   └── ci.yml                # Continuous Integration workflow
        └── ISSUE_TEMPLATE.md         # Template for GitHub issues -->
