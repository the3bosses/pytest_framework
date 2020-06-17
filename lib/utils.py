import os


def create_folder(folder_name):
    """Creates a folder if it does not exist"""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name
