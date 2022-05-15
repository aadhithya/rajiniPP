from . import runner


def test_print(hello_world, capsys):
    runner.exec(hello_world)
    out, err = capsys.readouterr()
    assert out.strip() == "Hello, World!"


def test_multi_print(multi_print, capsys):
    runner.exec(multi_print)
    out, err = capsys.readouterr()
    assert out.strip() == "5 + 5 = 10.0"
