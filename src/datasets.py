import json

def load_dataset(file_path):
    """
    Load a dataset from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing the dataset.

    Returns:
        list: A list of dictionaries representing the dataset.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

