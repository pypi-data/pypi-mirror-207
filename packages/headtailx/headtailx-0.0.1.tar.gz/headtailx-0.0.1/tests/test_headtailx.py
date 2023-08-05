import pytest
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
from headtailx.headtailx_common import HeadTail
import numpy as np


def create_test_dataframe():
    return pd.DataFrame(
        {
            "timestamp": [10, 20, 30, 40, 50, 60, 70, 80, 90],
            "flavor": [
                "strange",
                "up",
                "charm",
                "strange",
                "up",
                "charm",
                "strange",
                "up",
                "charm",
            ],
            "color": [
                "red",
                "blue",
                None,
                "red",
                "blue",
                "green",
                "red",
                "blue",
                "green",
            ],
            "foobar": [1, 2, 3, 4, 5, np.nan, 7, 8, 9][::-1],
            "floats": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
            "booleans": [True, False, True, False, True, False, True, False, True],
            "datetime": [datetime(2021, 1, 1) + timedelta(days=i) for i in range(9)],
            "timedelta": [timedelta(hours=i) for i in range(9)],
        }
    )


def read_file_head(file_path, num_lines=4):
    head_tail = HeadTail(file_path, num_lines=num_lines)
    head_str = head_tail.head()
    head_lines = head_str.strip().split("\n")
    return head_lines


@pytest.fixture
def df():
    return create_test_dataframe()


def save_test_files(df, tmp_path):
    file_names = {
        "csv": "test.csv",
        "feather": "test.feather",
        "pickle": "test.pickle",
        "parquet": "test.parquet",
        "hdf": "test.h5",
        "json": "test.json",
        "xlsx": "test.xlsx",
    }
    save_funcs = {
        "csv": df.to_csv,
        "feather": df.to_feather,
        "pickle": df.to_pickle,
        "parquet": df.to_parquet,
        "hdf": df.to_hdf,
        "json": df.to_json,
        "xlsx": df.to_excel,
    }
    save_args = {
        "csv": [],
        "feather": [],
        "pickle": [],
        "parquet": [],
        "hdf": ["/data"],
        "json": [],
        "xlsx": [],
    }

    save_kwargs = {
        "csv": {"sep": ","},
        "feather": {},
        "pickle": {},
        "parquet": {"compression": "gzip"},
        "hdf": {"format": "table", "complib": "blosc"},
        "json": {"orient": "records"},
        "xlsx": {"engine": "openpyxl"},
    }

    # test_files = save_test_files(df, tmp_path, save_args=save_args, save_kwargs=save_kwargs)

    for ext, file_name in file_names.items():
        save_func = save_funcs[ext]
        save_arg = save_args[ext]
        save_kwarg = save_kwargs[ext]
        file_path = tmp_path / file_name
        save_func(file_path, *save_arg, **save_kwarg)
    return {ext: tmp_path / file_name for ext, file_name in file_names.items()}


@pytest.fixture
def test_files(df, tmp_path):
    return save_test_files(df, tmp_path)


def test_head_tail(df, test_files):
    for ext, file_path in test_files.items():
        head_lines = read_file_head(file_path)
        newline: str = "\n"
        print(f"\nLoaded {ext} file:\n{newline.join(head_lines)}")

        assert "up" in head_lines[2]
        assert "10" in head_lines[1]
        assert "True" in head_lines[1]
