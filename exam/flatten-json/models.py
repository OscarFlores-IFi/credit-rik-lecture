import json

def load(filename):
    with open(filename, "r") as file:
        data = json.loads(file.read())
    return data
