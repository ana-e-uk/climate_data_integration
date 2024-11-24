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
1. *Best Practices:* Look into the climate science literature and determine the most common data format, grid, time range, variables, etc.. This will help us decide the framework to unify all datasets to.
2. *Unify Data Format:* The first thing to do will be to unify all the data to the same format that will make it easy to work with and store.
3. *Grid Data:* While some data is already gridded (def), data may use different grids, so all the data must be re-gridded to the same grid. Other data is not gridded, so it must be gridded or stored separately such that it is easy to use gridded and non-gridded data together.
4. *Consolidate Time Resolution:* Datapoints may be taken at varying time intervals. Here we determine what to do when points coincide, and when they don't. This could include merging data points, deleting redundant data, or developing a way to keep all the information with varying time intervals between points.
5. *Find Minimum Variable Set:* This is where we determine if the same variable has different names in different datasets. This is usually called column-matching. Datasets may have unique variables they measure, but there will be overlap as well. There exists a minimum set of variables where each element is a unique variable.
6. *Find Duplicates:* Some records may hold the same measurement for the same variable. If the value is exactly the same, we can just keep one. If the values are not the same, we can calculate some statistics about the measurement to give a more accurate idea to scientists regarding the range of this value.
7. *Manage Duplicates:* Provide various ways to handle duplicate data such as aggregating, deleting, etc..
8. *Join Similar Data:* Data may not be the same but may be useful to have together, such as the u component of the wind and the v component of the wind.
9. *Provide Metadata:* For the integrated data, provide useful metadata that keeps track of where data came from, the extent of information, aggregation methods, etc..

## Project Plan

**Determining Unified Framework**

**Code Data Integration**

**Evaluation**

## Data
