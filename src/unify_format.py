"""
Unifing all data to the same format.
"""

def unify_data_format(input_data, format_config):
    """
    Converts data to a unified format.

    Args:
        input_data: Input dataset in raw format (file path or in-memory object).
        format_config: Configuration for format conversion.

    Returns:
        unified_data: Dataset in the unified format.
    """
    # If input is a CSV, convert to NetCDF
    if input_data.endswith(".csv"):
        unified_data = convert_csv_to_netcdf(input_data, format_config)
    elif input_data.endswith(".nc"):
        unified_data = input_data  # Already in desired format
    else:
        raise ValueError(f"Unsupported input format: {input_data}")
    return unified_data
