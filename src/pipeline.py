from src.unify_format import unify_data_format
from src.variable_matching import match_variables
from src.regrid import regrid_data
from src.temporal_resolution import consolidate_time_resolution
from src.deduplicate import find_duplicates, manage_duplicates
from src.data_joining import join_similar_data
from src.metadata_generator import generate_metadata

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
    regridded_data = []

    for data in input_data:
        # Step 1: Unify data format to netcdf
        unified_data = unify_data_format(data)

        # Step 3: Re-grid data to [WGS 84]
        regridded_data.append(regrid_data(unified_data))

    # Step 2: Match variables
    standardized_data = match_variables(regridded_data)

    # Step 4: Consolidate time resolution
    time_consistent_data = consolidate_time_resolution(standardized_data, config.get("time"))

    # Step 5: Find duplicates
    duplicates = find_duplicates(time_consistent_data)

    # Step 6: Manage duplicates
    cleaned_data = manage_duplicates(time_consistent_data, duplicates, config.get("duplicate_handling"))

    # Step 7: Join similar data
    joined_data = join_similar_data(cleaned_data, config.get("join"))

    # Step 8: Generate metadata
    metadata = generate_metadata(joined_data, config.get("metadata"))

    return joined_data, metadata