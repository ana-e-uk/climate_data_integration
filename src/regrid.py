"""
Perform spatial re-gridding or handle un-gridded data separately.

Use tools like xarray and xarray_regrid.
"""

from config import standard_col_names

def regrid_data(input_data):
    """
    Regrid data that is not in the desired grid.

    Arg:
        input_data: File path of data that needs to be regridded.
        grid_config: Desired grid.
    """