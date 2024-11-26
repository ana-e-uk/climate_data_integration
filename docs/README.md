# climate_data_integration

This repository contains Ana Uribe and Nithya Nurikinati's final project code and documentation for CSCI 8735: Advanced Database Systems (Fall 2024).

## Introduction

We hope to create a Python-based software to integrate climate science data.

**Motivation:** Climate data is collected by different organizations and instruments such as satellites. For one region and time range, this could lead to:
* The exact same data being collected at the same time intervals and spatial grid.
* The exact same data being collected at different time intervals and/or different spatial grid.
* Similar or related data being collected at the same or different spatial and/or temporal resolutions.

Unifying these various datasets can help scientists analyze a region or time range of interest with all the available data.

**Data Integration Plan:** 
0. *Best Practices:* Look into the climate science literature and determine the most common data format, grid, time range, variables, etc.. This will help us decide the framework to unify all datasets to. Thus, all the steps below are subject to change due to current best practices.
1. *Unify Data Format:* The first thing to do will be to convert all incoming data to the same format.
2. *Variable Matching:* Incoming datasets may have different names for the same variables (such as temp. for temperature etc.), so starting with a set of expected values, we will have a process that checks all the columns of incoming datasets and “column-matches” the values or adds a new value to the set if there is a new value.
3. *Grid Data:* While some data is already [gridded](https://climateestimate.net/content/gridded-data.html#:~:text=These%20generally%20consist%20of%20combining,at%20each%20gridpoint%20and%20timestep.) (divided into latitude x longitude grid over the surface area of the Earth), data may use different grids, so all the data must be re-gridded to the same grid. Other data is not gridded, so it must be gridded or stored separately such that it is easy to use gridded and non-gridded data together.
4. *Consolidate Temporal Resolution:* Datapoints may be taken at varying time intervals. Here we determine what to do when points coincide, and when they don't. This could include merging data points, deleting redundant data, or developing a way to keep all the information with varying time intervals between points.
5. *Find Duplicates:* Some records may hold the same measurement for the same variable. If the value is exactly the same, we can just keep one. If the values are not the same, we can calculate some statistics about the measurement to give a more accurate idea to scientists regarding the range of this value.
6. *Manage Duplicates:* Provide various ways to handle duplicate data such as aggregating, deleting, etc..
7. *Join Similar Data:* Data may not be the same but may be useful to have together, such as the u component of the wind and the v component of the wind.
8. *Provide Metadata:* For the integrated data, provide useful metadata that keeps track of where data came from, the extent of information, aggregation methods, etc..

---
**More documentation on the data used, evaluation methods, and best practices in the `docs/` folder. Additionally, how to setup the environment, dependencies, guidelines for contributing, and detalis about the API and CLI are also in this folder.**

## Repository Layout

    project-root/
    ├── data/
    │   ├── raw/                      # Store raw incoming data files
    │   ├── processed/                # Store processed data files
    │   └── metadata/                 # Store metadata files
    ├── src/
    │   ├── pipeline.py               # Main pipeline function
    │   ├── unify_format.py           # Step 1 function of Data Integration Plan
    │   ├── variable_matching.py      # Step 2 function
    │   ├── regrid.py                 # Step 3 function
    │   ├── temporal_resolution.py    # Step 4 function
    │   ├── deduplicate.py            # Step 5 & 6 function
    │   ├── data_joining.py           # Step 7 function
    │   ├── metadata_generator.py     # Step 8 function
    │   └── utils.py                  # Common utilities
    ├── notebooks/                    # Jupyter notebooks for testing and visualization
    ├── tests/
    │   ├── test_unify_format.py
    │   ├── test_variable_matching.py
    │   ├── test_regrid.py
    │   ├── test_temporal_resolution.py
    │   ├── test_deduplicate.py
    │   ├── test_data_joining.py
    │   └── test_metadata_generator.py
    ├── docs/
    │   ├── README.md                 # Overview of the project
    │   ├── CONTRIBUTING.md           # Guidelines for contributing
    │   ├── requirements.txt          # Dependencies
    │   ├── setup.md                  # Instructions to set up the environment
    │   ├── API.md                    # Details about the API and CLI
    │   ├── best_practices.md                 # Description of each step
    │   ├── data.md                 # Overview of the data used
    │   └── evaluation.md                 # Description of the evaluation of each step
    ├── config/
    │   ├── variable_mapping.json     # Configuration for variable matching
    │   ├── grid_config.yaml          # Configuration for re-gridding
    │   ├── metadata_template.yaml    # Metadata structure template
    │   └── config.yaml               # General project configuration
    ├── scripts/
    │   ├── integrate_data.py           # Script to run the full data processing pipeline
    │   ├── preprocess_data.sh        # Example shell script for data preprocessing
    │   └── analyze_output.sh         # Example script for analyzing outputs
    <!-- └── .github/
        ├── workflows/
        │   └── ci.yml                # Continuous Integration workflow
        └── ISSUE_TEMPLATE.md         # Template for GitHub issues -->
