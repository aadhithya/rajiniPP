import pytest
from rajinipp import api


def test_print(hello_world, capsys):
    api.exec(hello_world)
    out, err = capsys.readouterr()
    assert out.strip() == "Hello, World!"


def test_multi_print(multi_print, capsys):
    api.exec(multi_print)
    out, err = capsys.readouterr()
    assert out.strip() == "5 + 5 = 10.0"