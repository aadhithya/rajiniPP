import os
from pathlib import Path

import pytest

# * project root dir
root_dir = Path(__file__).parents[1]

# * rpp programs dir to run tests
rpp_dir = os.path.join(root_dir, "examples")


def read_file(file_path: str):
    with open(file_path, "r") as file:
        return file.read()


@pytest.fixture
def hello_world():
    return read_file(os.path.join(rpp_dir, "hello_world.rpp"))


@pytest.fixture
def multi_print():
    return read_file(os.path.join(rpp_dir, "multi_print.rpp"))
