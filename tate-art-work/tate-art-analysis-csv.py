# Read data from the csv.
# open csv, create a dataframe with the required columns from the csv

import pandas as pd
import os


def read_artwork_from_csv(file):

    cols_to_use = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']
    df = pd.read_csv(file, index_col="id", usecols=cols_to_use)
    return df


csv_path = os.getcwd() + '/collection-master/artwork_data.csv'
df = read_artwork_from_csv(csv_path)




