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


# Some analysis:

print('\nSome analysis: \n')

# number of unique artists in the data
artists = df['artist']
unique_artists = pd.unique(artists)
print(f'There are {len(unique_artists)} unique artists in the database.\n')

# Number of artworks by a specific artist
artist_counts = df['artist'].value_counts()
print(f"Artist Francis Bacon has {artist_counts['Bacon, Francis']} artworks in the database. \n")

# Find the largest artwork (by area)
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')
df['area'] = df['height'] * df['width']
print(f"The largest artwork is {df.loc[df['area'].idxmax(), :]}.")


