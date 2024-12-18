"""
Common utilities throughout src.
"""
import os

def new_file_path(path, new_folder, add):
    # save new dataset
    directory, file_name = os.path.split(path)
    parent_directory = os.path.dirname(directory)

    new_file_name = add + file_name
    updated_file_path = os.path.join(parent_directory, new_folder, new_file_name)

    return updated_file_path