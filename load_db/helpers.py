import json
import os
import configparser
import boto3
from pathlib import Path

from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
  """
  Class to decode json-Decimal Objects to Strings, so they can be written to a json-file.
  Inherits from json.JSONEncoder
  """
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

def get_path_to_data():
    """Return path to data."""
    return Path('Data/')


def get_raw_data_path():
    """Return path to raw data."""
    return get_path_to_data() / 'RawMovieData.json'


def get_tidy_data_path():
    """Return path to tidy data."""
    return get_path_to_data() / 'TidyMovieData.parquet'
