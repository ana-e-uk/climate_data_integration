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
**Information about data integration and deduplication, and the data used for this project is in the `docs/` folder. Additionally, how to setup the environment is also in this folder.**

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
    ├── docs/
    │   ├── README.md                 # Overview of the project         <-- PROJECT
    │   ├── CONTRIBUTING.md           # Guidelines for contributing
    │   ├── setup.md                  # Instructions to set up the environment  <-- PROJECT
    │   ├── API.md                    # Details about the API and CLI
    │   ├── process_info.md           # Description of each step        <-- PROJECT
    │   ├── data.md                   # Overview of the data used       <-- PROJECT
    │   └── evaluation.md             # Description of the evaluation of each step  <-- PROJECT
    ├── config/
    │   ├── variable_mapping.json     # Configuration for variable matching
    │   ├── grid_config.yaml          # Configuration for re-gridding
    │   ├── metadata_template.yaml    # Metadata structure template     <-- PROJECT
    │   └── config.yaml               # General project configuration   <-- PROJECT
    ├── scripts/
    |   ├── deduplicate_data.py       # Script to run the data deduplication        <-- PROJECT
    │   ├── integrate_data.py         # Script to run the full data integration pipeline
    │   ├── preprocess_data.sh        # Example shell script for data processing
    │   └── analyze_output.sh         # Example script for analyzing outputs        <-- PROJECT
    ├── requirements.txt              # Dependencies      <-- PROJECT
    └── .gitignore      <-- PROJECT

<!-- └── .github/
        ├── workflows/
        │   └── ci.yml                # Continuous Integration workflow
        └── ISSUE_TEMPLATE.md         # Template for GitHub issues -->
