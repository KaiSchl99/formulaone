import pandas as pd
import json
from load_db.helpers import get_raw_data_path, get_tidy_data_path


def clean_and_write_data():
    """
    cleans and writes data to parquet file
    """
    # Pfad zur JSON-Datei erhalten
    json_file_path = get_raw_data_path()

    # JSON-Datei laden
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # JSON-Daten normalisieren und in DataFrame umwandeln
    df = pd.json_normalize(data['Items'], 
                        meta=['title', 'year', ['info', 'rating'], ['info', 'rank'], ['info', 'plot'], ['info', 'genres']],
                        record_path=['info', 'actors'],
                        errors='ignore')

    # Umbenennen der "0"-Spalte in "actor"
    df.rename(columns={0: 'actor'}, inplace=True)

    # Listen in Strings umwandeln
    df['info.genres'] = df['info.genres'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)

    # Split genres into separate rows
    df = df.assign(genres=df['info.genres'].str.split(', ')).explode('genres')

    df.drop(columns=['info.genres'], inplace=True)

    path_to_save = get_tidy_data_path()
    df.to_parquet(path_to_save)


# Ausgabe des "tidy" DataFrames
clean_and_write_data()


