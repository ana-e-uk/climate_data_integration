"""
Unifing all data to the same format and grid [WGS 84].
"""
import xarray as xr

def convert_csv_to_netcdf(d, c):
    """
    Convert csv to netcdf.

    Args:
        d: File path to a csv.
        c: Configuration for format conversion.
    """

def convert_json_to_netcdf(d, c):
    """
    Convert json to netcdf.

    Args:
        d: File path to a json.
        c: Configuration for format conversion.
    """

def check_grid(nc_file):
    """
    Check the grid type used in a NetCDF file.
    
    Args:
        nc_file (str): Path to the NetCDF file.
        
    Returns:
        grid mapping name (str)
    """
    try:
        ds = xr.open_dataset(nc_file)
        
        # Check global attributes for grid type information
        if 'grid_mapping_name' in ds.attrs:
            return f"Grid Mapping: {ds.attrs['grid_mapping_name']}"
        
        # Search for a variable specifying the CRS or grid mapping
        for var_name, var in ds.variables.items():
            if 'grid_mapping_name' in var.attrs:
                grid_mapping_name = var.attrs['grid_mapping_name']
                crs_info = f"Grid Mapping: {grid_mapping_name}"
                
                # Additional details like datum and projection
                if 'datum' in var.attrs:
                    crs_info += f", Datum: {var.attrs['datum']}"
                if 'earth_radius' in var.attrs:
                    crs_info += f", Earth Radius: {var.attrs['earth_radius']} meters"
                if 'semi_major_axis' in var.attrs and 'semi_minor_axis' in var.attrs:
                    crs_info += f", Semi-Major Axis: {var.attrs['semi_major_axis']} m, Semi-Minor Axis: {var.attrs['semi_minor_axis']} m"
                return crs_info
        
        # Check for commonly used CRS variable names
        crs_var_candidates = ['crs', 'spatial_ref']
        for crs_var in crs_var_candidates:
            if crs_var in ds.variables:
                crs_attrs = ds[crs_var].attrs
                return f"CRS Attributes: {crs_attrs}"
        
        # Fallback if no CRS information is found
        return "No CRS or grid mapping information found in the file."
    
    except Exception as e:
        return f"Error: {e}"

def unify_data_format(input_data):
    """
    Converts data to a unified format.

    Args:
        input_data: An input dataset in file path format.

    Returns:
        unified_data: Dataset file path in the unified format.
        grid_type: String that denotes the grid type information.
    """
    # Convert to same format
    if input_data.endswith(".csv"):
        unified_data = convert_csv_to_netcdf(input_data)
    elif input_data.endswith(".json"):
        unified_data = convert_json_to_netcdf(input_data)
    elif input_data.endswith(".nc"):
        unified_data = input_data  # Already in desired format
    else:
        print(f"Unsupported input format: {input_data}")
    
    # Check grid is the same
    grid_type = check_grid(unified_data)

    return unified_data, grid_type

