from src.unify_format import unify_data_format
from src.variable_matching import match_variables
from src.temporal_resolution import consolidate_time_resolution
from src.match import aggregate_overlaps

import os

import config

def integration_pipeline(input_data, output_file, scaling_factors, variable, aggregation_func):
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

    processed_data_list = []

    for data in standardized_data:
        unified_data, grid_type = unify_data_format(data)
        print(f"File: {os.path.basename(data)} \tGrid type: {grid_type}")
        
        time_consistent_data = consolidate_time_resolution(unified_data)

        processed_data_list.append(time_consistent_data)

    aggregate_overlaps(file_list=processed_data_list, 
                              scaling_factors=scaling_factors, 
                              output_file=output_file, 
                              aggregation_func=aggregation_func, 
                              time_dim=config.TIME, 
                              lat_dim=config.LAT, 
                              lon_dim=config.LONG, 
                              variable=variable)
    