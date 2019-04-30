import json

def read_json_data_file(filename):
    objs = []
    with open(filename, errors='replace') as file:
        for line in file:
            objs.append(json.loads(line))
    return objs
