"""
Perform spatial re-gridding or handle un-gridded data separately.

Use tools like xarray and xarray_regrid.
"""

def regrid_data(input_data, grid_config):
    """
    Regrid data that is not in the desired grid.

    Arg:
        input_data: File path of data that needs to be regridded.
        grid_config: Desired grid.
    """