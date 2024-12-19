"""
Detect and handle duplicate records using user-defined rules (e.g., averaging, retaining max/min values).
"""
import os
import json
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

import src.config

def drop_unwanted_dims(ds):
    """
    Drops any dimension from the dataset that is not in the list of dimensions to keep.

    Args:
        ds (xarray.Dataset): The dataset from which to drop dimensions.

    Returns:
        xarray.Dataset: The dataset with unwanted dimensions dropped.
    """
    keep_dims = ['datetime', 'latitude', 'longitude', 'sea_ice_temp']
    drop_dims = [dim for dim in ds.dims if dim not in keep_dims]
    ds = ds.drop_dims(drop_dims, errors="ignore")  # Avoid errors if a dimension is already dropped
    return ds

def aggregate_overlaps(file_list, scaling_factors, variable, aggregation_func):
    """
    Aggregate overlapping regions between two datasets.
    """
    # Create scaling factors if not provided
    if scaling_factors is None:
        scaling_factors = [1] * len(file_list)
    # Check if scaling_factors matches the number of files
    if len(scaling_factors) != len(file_list):
        raise ValueError("Length of scaling_factors must match length of file_list.")

    # Create datasets and scale variables
    ds_list = []
    for file, scale in zip(file_list, scaling_factors):
        ds = drop_unwanted_dims(xr.open_dataset(file))
        ds[variable] = ds[variable] * scale
        ds_list.append(ds)
    
    aggregated = ds_list[0]
    for ds2 in ds_list[1:]:
        aligned_ds1, aligned_ds2 = xr.align(aggregated, ds2, join="inner")

        # Apply aggregation function
        if aggregation_func == "mean":
            aggregated[variable] = (aligned_ds1[variable] + aligned_ds2[variable])
        elif aggregation_func == "min":
            aggregated[variable] = xr.ufuncs.minimum(aligned_ds1[variable], aligned_ds2[variable])
        elif aggregation_func == "max":
            aggregated[variable] = xr.ufuncs.maximum(aligned_ds1[variable], aligned_ds2[variable])
        elif aggregation_func == "sum":
            aggregated[variable] = aligned_ds1[variable] + aligned_ds2[variable]
        else:
            raise ValueError(f"Unsupported aggregation function: {aggregation_func}")

    return aggregated
