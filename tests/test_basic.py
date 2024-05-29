# content of test_sample.py
# Datei muss immer mit "test_" anfangen

from load_db.helpers import get_tidy_data_path
import pandas as pd


def test_check_dataframe_size():
    a = 1
    assert a == 1
