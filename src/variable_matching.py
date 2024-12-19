"""
Implement variable name standardization based on a predefined set of mappings.

Update mappings dynamically for new variables.
"""
import xarray as xr
import os

from src.utils import new_file_path

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

def convert_col_names(data, standard_col_names):
    """
    Rename the columns (dimensions/variables) of an xarray.Dataset based on a mapping dictionary.
    
    Args:
        standard_col_names (dict): A dictionary where keys are standard names and values are lists of possible names.
        dataset (xarray.Dataset): The xarray dataset whose column/dimension names need to be renamed.
    
    Returns:
        xarray.Dataset: A new dataset with renamed columns (dimensions/variables).
    """
    # Create a mapping from the dataset's current column names to the new standardized names
    rename_mapping = {}
    
    # Iterate through the dictionary to identify names to rename
    for standard_name, possible_names in standard_col_names.items():
        for current_name in data.dims.keys():  # Check dimension names
            if current_name in possible_names:
                rename_mapping[current_name] = standard_name
        for current_name in data.data_vars.keys():  # Check variable names
            if current_name in possible_names:
                rename_mapping[current_name] = standard_name

    # Apply the renaming to the dataset
    renamed_dataset = data.rename(rename_mapping)

    return renamed_dataset

def match_variables(input_data, standard_col_names):
    """
    Column-match the columns with the same information

    Args:
        input_data: List of datasets in file path format.
        var_config: Standard variable set for conversion.

    Returns:
        output_data: List of datasets in file path format, all with
        standard variable/dimension names.
    """
    output_data = []

    for path in input_data:
        data = xr.open_dataset(path, engine="netcdf4")

        # get new dataset with standard col names
        standard_data = drop_unwanted_dims(convert_col_names(data, standard_col_names))

        updated_file_path = new_file_path(path, "processed", "st_cols_")
        standard_data.to_netcdf(updated_file_path)
        output_data.append(updated_file_path)

    return output_data