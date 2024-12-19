"""
Detect and standardize temporal resolutions across datasets.

Add metadata annotations about the resolution.
"""
import xarray as xr
import pandas as pd

from src.utils import new_file_path

def consolidate_time_resolution(input_data, time_dim):
    """
    Standardize time resolution to monthly.

    Arg:
        input_data: An input dataset in file path format.
        time_dim: Name of time dimension (str).
    """
    # Calculate time resolution
    cur_res = ""
    try:
        # Open the dataset
        ds = xr.open_dataset(input_data)

        # Convert the time dimension to a pandas datetime index
        time_values = pd.to_datetime(ds[time_dim].values)
        
        # Calculate the differences between consecutive timestamps
        time_deltas = pd.Series(time_values).diff().dropna()
        
        # Analyze the mode of the time differences
        mode_delta = time_deltas.mode()[0]
        
        # Determine the resolution based on the mode
        if mode_delta.days >= 28 and mode_delta.days <= 31:
            cur_res = "M"
        elif mode_delta.days == 1:
            cur_res = "D"
        elif mode_delta.seconds == 3600:
            cur_res = "H"
        elif mode_delta.seconds == 60:
            cur_res = "min"
        elif mode_delta.seconds == 1:
            cur_res = "S"
        else:
            return f"Unknown resolution: {mode_delta}"
    
    except Exception as e:
        return f"Error: {e}"

    # Resample temporal resolution to monthly
    print(f"\tTemporal resolution: {cur_res}")
    ds = ds.resample(time_dim = "ME").mean()
    
    updated_file_path = new_file_path(input_data, "processed", "monthly_")
    ds.to_netcdf(updated_file_path)

    return updated_file_path