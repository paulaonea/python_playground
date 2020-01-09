# Read data from json files.
# identify all files, read required data, create list of tuple, create dataframe

import os
import json
import pandas as pd


def get_record_from_file(file_path, keys):
    with open(file_path) as file:
        content = json.load(file)
    record = []
    for field in keys:
        record.append(content[field])

    return tuple(record)


def read_artwork_from_json(keys):
    json_root = os.getcwd() + '/collection-master/artworks'
    artworks = []
    for root, _, files in os.walk(json_root):
        for f in files:
            if f.endswith('json'):
                record = get_record_from_file(os.path.join(root, f), key_to_use)
                artworks.append(record)
            break
    dataf = pd.DataFrame.from_records(artworks, columns=key_to_use, index='id')
    return dataf


key_to_use = ['id', 'all_artists', 'title', 'medium', 'acquisitionYear', 'height', 'width', 'units']
df = read_artwork_from_json(key_to_use)
