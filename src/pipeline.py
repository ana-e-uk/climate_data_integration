from src.unify_format import unify_data_format
from src.variable_matching import match_variables
from src.temporal_resolution import consolidate_time_resolution
from src.match import find_matches, manage_matches

import config

def integration_pipeline(input_data, config):
    """
    Orchestrates the data integration pipeline.

    Args:
        input_data: List of file path names of the datasets to be integrated.
        config: Configuration dictionary with settings for each step.

    Returns:
        integrated_data: Final integrated dataset.
        metadata: Metadata for the integrated data.
    """
    standardized_data = match_variables(input_data, config.standard_col_names)

    unified_data_list = []

    for data in standardized_data:
        unified_data, grid_type = unify_data_format(data)
        print(f"File: {data} \tGrid type: {grid_type}")
        
        unified_data_list.append(unified_data)

    # Step 4: Consolidate time resolution
    time_consistent_data = consolidate_time_resolution(standardized_data)

    # Step 5: Find duplicates
    matches = find_matches(time_consistent_data)

    # Step 6: Manage duplicates
    integrated_data, metadata = manage_matches(time_consistent_data, matches, config.MANAGE)

    return integrated_data, metadata