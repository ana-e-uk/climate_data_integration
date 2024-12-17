"""
Unifing all data to the same format.
"""


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

def unify_data_format(input_data, format_config):
    """
    Converts data to a unified format.

    Args:
        input_data: An input dataset in file path format.
        format_config: Configuration for format conversion.

    Returns:
        unified_data: Dataset file path in the unified format.
    """
    # If input is a CSV, convert to NetCDF
    if input_data.endswith(".csv"):
        unified_data = convert_csv_to_netcdf(input_data)
    elif input_data.endswith(".json"):
        unified_data = convert_json_to_netcdf(input_data)
    
    # Add more cases for different data formats

    elif input_data.endswith(".nc"):
        unified_data = input_data  # Already in desired format
    else:
        print(f"Unsupported input format: {input_data}")
    
    return unified_data