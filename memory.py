import json

def read_json_from_file(filename = 'data.txt'):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def create_and_write_json_to_file(data, filename='data.txt'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


