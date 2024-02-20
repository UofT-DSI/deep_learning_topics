import json
import yaml

def read_yaml_json_to_dict(path: str) -> dict:
    if not isinstance(path, str):
        raise ValueError("Input should be a path to a YAML/JSON file as a string.")

    # Check the file extension
    extension = path.split(".")[-1].lower()

    with open(path, "r") as file:
        if extension == "yaml" or extension == "yml":
            return yaml.safe_load(file)
        elif extension == "json":
            return json.load(file)
        else:
            raise ValueError(
                "Unsupported file format. Please provide a YAML or JSON file."
            )