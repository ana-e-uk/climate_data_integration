# Data Documentation

<!-- There is a lot of different data repositories available that we can use to get data and show our integration methods. There are also different types of datasets, some of which generate the others, and thus should not be "re-aggregated". Thus, we will have to determine what to do when "combining/unifying/integrating" these different types of datasets. -->
There are a lot of different climate data repositories. Below is a general overview of the climate science data landscape, and then the specific data we used to test our deduplication methods.

## Data Repositories List

* [NOAA](https://psl.noaa.gov/data/gridded/)
* [CDS](https://cds.climate.copernicus.eu)
* [AMRDC](https://amrdcdata.ssec.wisc.edu)
* [Artic Data Center](https://arcticdata.io)
* [ESDS](https://earthdata.nasa.gov_)
* [SENTINEL](https://sentinels.copernicus.eu/web/sentinel/home)

## Types of Datasets

* Analysis (data in database from sources)
* Reanalysis (weather observations + computer model = global weather)
* Forecast (historical data → future predictions)
* Reforecast (reanalysis → “future” predictions)
* Climate simulation (science + factors = scenarios)

## Data Used
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