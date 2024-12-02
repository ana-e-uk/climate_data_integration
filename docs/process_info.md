# Process Information

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
