"""
Script to run the full data integration pipeline
"""
import os

from src.pipeline import integration_pipeline

if __name__ == "__main__":

    print(f"\nBeginning Data Integration.\nPlease enter the following:\n")
    input_data_dir = input("\nDirectory of files to integrate:").strip()
    input_data = [f for f in os.listdir(input_data_dir) if os.path.isfile(os.path.join(input_data_dir, f))]

    output_file = input("\nIntegrated file path:").strip()

    scaling_factors = []

    for f in input_data:
        factor = input(f"\n\tScaling factor of dataset {os.path.basename(f)}:").strip()
        scaling_factors.append(factor)

    variable = input("\nVariable to integrate:").strip()

    aggregation_func = input("\nAggregation function - choose out of [mean, min, max, sum]:").strip()

    integration_pipeline(input_data, output_file, scaling_factors, variable, aggregation_func)