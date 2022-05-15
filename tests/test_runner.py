from . import runner


def test_exec(hello_world, capsys):
    runner.exec(hello_world)
    out, err = capsys.readouterr()
    assert out.strip() == "Hello, World!"


def test_eval():
    out = runner.eval("5+5;")
    assert out == 10.0
