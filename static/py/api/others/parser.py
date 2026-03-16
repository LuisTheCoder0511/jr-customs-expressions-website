import json

def parse_lob_data(data):
    if not (data == dict):
        str_data = str(data)
        data = json.loads(str_data)

    return data
