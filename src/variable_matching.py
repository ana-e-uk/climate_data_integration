"""
Implement variable name standardization based on a predefined set of mappings.

Update mappings dynamically for new variables.
"""

def match_variables(input_data, var_config):
    """
    Column-match the columns with the same 

    Args:
        input_data: Input dataset in file path format.
        var_config: Standard variable set for conversion.
    """
    # Get column names of all files in input_data
    # Check if there are matching columns
    # Convert matching columns to one column name and one unit
    # Return list of new files with the correct column names/units
    # List can have old file names if there was no change to that file