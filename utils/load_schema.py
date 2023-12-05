import json


def load_schema(path):
    with open(path) as f:
        schema = json.load(f)
        return schema
