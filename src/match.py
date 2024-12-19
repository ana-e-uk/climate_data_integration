"""
Detect and handle duplicate records using user-defined rules (e.g., averaging, retaining max/min values).
"""
import os
import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
pseudo-code:

for every pair of files:

    get the common region, and the regions where they don't overlap.
    aggregate the overlapping regions the way we want and append the regions where they don't overlap
    this will result in one final file that has the union of all the time and location points of all the files,
    and also gets the file

'''
import xarray as xr
import numpy as np

def aggregate_and_merge_files(file_list, scaling_factors, output_file, aggregation_func, time_dim, lat_dim, lon_dim, variable):
    """
    Aggregate and merge a list of NetCDF files into one file, considering overlapping regions.
    Saves the merged dataset to 'output_file'.
    
    Args:
        file_list (list): List of file paths to NetCDF files.
        scaling_factors (list): List of scaling factors (floats) corresponding to the list of files.
        output_file (str): Path to save the final merged NetCDF file.
        aggregation_func (str): Aggregation function for overlapping regions ("mean", "min", "max", "sum").
        time_dim (str): Name of the time dimension.
        lat_dim (str): Name of the latitude dimension.
        lon_dim (str): Name of the longitude dimension.
        variable (str): Variable to aggregate and merge.
    
    Returns:
        overlap_info
    """
    # Open the first file to initialize the combined dataset
    combined_ds = xr.open_dataset(file_list[0])

    if scaling_factors is None:
        scaling_factors = [1] * len(file_list)
    scaled_data_list = []

    overlap_info = {}
    past_file = os.path.basename(file_list[0])
    
    # Loop through the rest of the files
    for file, scale in zip(file_list[1:], scaling_factors):
        current_ds = xr.open_dataset(file)

        # Rescale variable column values
        current_ds[variable] = current_ds[variable] * scale

        # Find common overlapping regions in all dimensions
        overlap_time = np.intersect1d(combined_ds[time_dim], current_ds[time_dim])
        overlap_lat = np.intersect1d(combined_ds[lat_dim], current_ds[lat_dim])
        overlap_lon = np.intersect1d(combined_ds[lon_dim], current_ds[lon_dim])

        overlap_info[f"{past_file} & {os.path.basename(file)}"] = {"time": overlap_time, "latitude": overlap_lat, "longitude": overlap_lon}
        past_file = os.path.basename(file)

        # Extract overlapping data
        if overlap_time.size > 0 and overlap_lat.size > 0 and overlap_lon.size > 0:
            combined_overlap = combined_ds.sel(
                {time_dim: overlap_time, lat_dim: overlap_lat, lon_dim: overlap_lon}
            )
            current_overlap = current_ds.sel(
                {time_dim: overlap_time, lat_dim: overlap_lat, lon_dim: overlap_lon}
            )
            # Concatenate overlapping data along a new dimension for aggregation
            stacked_overlap = xr.concat(
                [combined_overlap[variable], current_overlap[variable]],
                dim="source"
            )

            # Aggregate the overlapping data
            if aggregation_func == "mean":
                aggregated_overlap = stacked_overlap.mean(dim="source")
            elif aggregation_func == "min":
                aggregated_overlap = stacked_overlap.min(dim="source")
            elif aggregation_func == "max":
                aggregated_overlap = stacked_overlap.max(dim="source")
            elif aggregation_func == "sum":
                aggregated_overlap = stacked_overlap.sum(dim="source")
            else:
                raise ValueError(f"Unsupported aggregation function: {aggregation_func}")
        else:
            aggregated_overlap = None  # No overlap

        # Extract non-overlapping data from each file
        combined_non_overlap = combined_ds.where(
            ~combined_ds[time_dim].isin(overlap_time) |
            ~combined_ds[lat_dim].isin(overlap_lat) |
            ~combined_ds[lon_dim].isin(overlap_lon),
            drop=True,
        )
        current_non_overlap = current_ds.where(
            ~current_ds[time_dim].isin(overlap_time) |
            ~current_ds[lat_dim].isin(overlap_lat) |
            ~current_ds[lon_dim].isin(overlap_lon),
            drop=True,
        )

        # Combine aggregated overlap with non-overlapping regions
        merged = xr.Dataset()
        if aggregated_overlap is not None:
            merged[variable] = aggregated_overlap
        if combined_non_overlap[variable].size > 0:
            merged = xr.merge([merged, combined_non_overlap])
        if current_non_overlap[variable].size > 0:
            merged = xr.merge([merged, current_non_overlap])

        # Update the combined dataset for the next iteration
        combined_ds = merged

    # Save the final merged dataset to a NetCDF file
    combined_ds.to_netcdf(output_file)
    print(f"Merged file saved to {output_file}")

    return overlap_info