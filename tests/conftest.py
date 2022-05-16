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


@pytest.fixture
def cond_code():
    return read_file(os.path.join(rpp_dir, "if_conditional.rpp"))


@pytest.fixture
def logic_code():
    return read_file(os.path.join(rpp_dir, "logical_ops.rpp"))


@pytest.fixture
def math_code():
    return read_file(os.path.join(rpp_dir, "math_ops.rpp"))


@pytest.fixture
def if_else_code():
    return read_file(os.path.join(rpp_dir, "if_else_conditional.rpp"))


@pytest.fixture
def for_loop_code():
    return read_file(os.path.join(rpp_dir, "for_loop.rpp"))


@pytest.fixture
def while_loop_code():
    return read_file(os.path.join(rpp_dir, "while_loop.rpp"))


@pytest.fixture
def fn_code():
    return read_file(os.path.join(rpp_dir, "functions_no_args.rpp"))


@pytest.fixture
def fn_return_code():
    return read_file(os.path.join(rpp_dir, "function_return.rpp"))
