"""
Detect and handle duplicate records using user-defined rules (e.g., averaging, retaining max/min values).
"""
import os
import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import config
'''
pseudo-code:

for every pair of files:

    get the common region, and the regions where they don't overlap.
    aggregate the overlapping regions the way we want and append the regions where they don't overlap
    this will result in one final file that has the union of all the time and location points of all the files,
    and also gets the file

'''

def get_common_regions(file_1, file_2, time_dim, lat_dim, lon_dim, variable):
    """
    Get the overlapping regions (time, latitude, longitude) between two files.

    Parameters:
        file_1, file_2 (list): List of file paths to NetCDF files.
        time_dim (str): Name of the time dimension.
        lat_dim (str): Name of the latitude dimension.
        lon_dim (str): Name of the longitude dimension.
        variable (str): Variable to compare between files.

    Returns:
        dict: Overlapping regions for time, latitude, and longitude.
    """
    d_1 = xr.open_dataset(file_1)
    d_2 = xr.open_dataset(file_2)

    # Find the common overlapping indices
    common_time = d_1[0][time_dim]
    common_lat = d_1[0][lat_dim]
    common_lon = d_1[0][lon_dim]

    common_time = np.intersect1d(common_time, d_2[time_dim])
    common_lat = np.intersect1d(common_lat, d_2[lat_dim])
    common_lon = np.intersect1d(common_lon, d_2[lon_dim])

    return {"time": common_time, "latitude": common_lat, "longitude": common_lon}


def find_matches(input_data_paths, time_dim, lat_dim, lon_dim, variable):
    """
    Check if NetCDF input_data overlap in time and space.

    Args:
        input_data_paths (list): List of file paths to NetCDF input_data.
        time_dim (str): Name of the time dimension.
        lat_dim (str): Name of the latitude dimension.
        lon_dim (str): Name of the longitude dimension.
        variable (str): Variable to compare between input_data.
    
    Returns:
        dict: A dictionary containing overlapping indices for time and space for each file pair.
    """
    datasets = [xr.open_dataset(f) for f in input_data_paths]
    input_data = [os.path.basename(f) for f in input_data_paths]
    overlap_info = {}

    aggregated_data = 

    for i, ds1 in enumerate(datasets):
        for j, ds2 in enumerate(datasets[i+1:], start=i+1):

            d = get_common_regions(input_data[i], input_data[j], config.time_dim, config.lat_dim, config.lon_dim, variable)

            overlap_info[f"{input_data[i]} & {input_data[j]}"] = d


            # Select overlapping data
            data1 = ds1[variable].sel(
                {time_dim: d["time"], lat_dim: d["latitude"], lon_dim: d["longitude"]}
            ).values.flatten()
            data2 = ds2[variable].sel(
                {time_dim: d["time"], lat_dim: d["latitude"], lon_dim: d["longitude"]}
            ).values.flatten()

            # Plot histogram and boxplot for comparison
            plt.figure(figsize=(12, 6))
            plt.subplot(1, 2, 1)
            plt.hist(data1, bins=30, alpha=0.5, label=f"{input_data[i]}")
            plt.hist(data2, bins=30, alpha=0.5, label=f"{input_data[j]}")
            plt.legend()
            plt.title("Histogram of Overlapping Values")

            plt.subplot(1, 2, 2)
            plt.boxplot([data1, data2], labels=[f"{input_data[i]}", f"{input_data[j]}"])
            plt.title("Boxplot of Overlapping Values")

            directory, file_name = os.path.split(input_data_paths[i])
            parent_directory = os.path.dirname(directory)
            fig_name = os.path.join(parent_directory, "figures", f"{input_data[i]} & {input_data[j]}_overlap.png")
            plt.savefig(fig_name, dpi=300)

    return overlap_info

def manage_matches(input_data_paths, output_file, scaling_factors, variable, aggregation_func):
    """
    Aggregate overlapping data and create a new NetCDF file.
    
    Args:
        input_data_paths (list): List of file paths to NetCDF files.
        output_file (str): Path to save the aggregated NetCDF file.
        scaling_factors (list): List of scaling factors for each file.
        variable (str): Variable to aggregate.
        aggregation_func (str): Method of aggregation (mean, max, min, sum).
    
    Returns:
        aggregated_data: File path to aggregated data file.
    """
    datasets = [xr.open_dataset(f) for f in input_data_paths]

    if scaling_factors is None:
        scaling_factors = [1] * len(input_data_paths)
    
    # Ensure scaling factors match the number of files
    assert len(scaling_factors) == len(input_data_paths), "Scaling factors must match the number of files."
    
    # List to store scaled variables
    scaled_data_list = []

    for ds, scale in zip(datasets, scaling_factors):
        # Scale the variable
        scaled_data = ds[variable] * scale
        scaled_data_list.append(scaled_data)

    # Combine all datasets along a new "source" dimension
    combined_data = xr.concat(scaled_data_list, dim="source")

    # Apply the chosen aggregation function along the "source" dimension
    if aggregation_func == "mean":
        aggregated_data = combined_data.mean(dim="source")
    elif aggregation_func == "min":
        aggregated_data = combined_data.min(dim="source")
    elif aggregation_func == "max":
        aggregated_data = combined_data.max(dim="source")
    elif aggregation_func == "sum":
        aggregated_data = combined_data.sum(dim="source")
    else:
        raise ValueError(f"Unsupported aggregation function: {aggregation_func}. Choose from 'mean', 'min', 'max', 'sum'.")

    # Save the aggregated data to a new file
    aggregated_data.to_netcdf(output_file)
    print(f"Aggregated data saved to {output_file}")