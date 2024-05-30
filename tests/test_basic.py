# content of test_sample.py
# Datei muss immer mit "test_" anfangen

from load_db.helpers import get_tidy_data_path
import pandas as pd
import boto3
import configparser


def test_tables_in_db():
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

    tables = []
    for table in dynamo_resource.tables.all():
        tables.append(table.name)
    
    print(tables)

    assert tables == ["doc-example-table-movies", "json_test"]
