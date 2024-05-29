import json
import requests
import configparser
import boto3
import os
from pathlib import Path
from boto3.dynamodb.conditions import Key

from load_db.helpers import DecimalEncoder


def connect_to_db():
    """
    Connect to Database with keys from Config file 'config.ini'. 
    Programs must be run from base directory for path to work!
    """
    config = configparser.ConfigParser()
    config.read("config.ini")

    access_key = config.get('Database', 'AccessKey')
    secret_key = config.get('Database', 'SecretKey')

    session = boto3.Session(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key
    )

    dynamo_resource = session.resource(
        'dynamodb',
        region_name='eu-west-1'
    )

    return session, dynamo_resource


def load_movies():
    """
    Loads the Movies of the year 2013 and returns the dictionary with all entries
    """
    session, dynamo_resource = connect_to_db()

    movies = dynamo_resource.Table('doc-example-table-movies')
    data = movies.query(
        KeyConditionExpression=Key('year').eq(2013)
    )

    return data


def write_loaded_movies():
    """
    Writes the loaded Movies to a json file
    """
    data = load_movies()

    json_object = json.dumps(data, indent=4, cls=DecimalEncoder)

    with open("./Data/RawMovieData.json", "w") as outfile:
        outfile.write(json_object)
    
    print("Data successfully written!")


def main():
    write_loaded_movies()
    # connect_to_db()


if __name__ == "__main__":
    main()