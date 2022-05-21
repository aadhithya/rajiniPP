from rajinipp import rpp


def test_exec(hello_world, capsys):
    rpp.exec(hello_world)
    out, err = capsys.readouterr()
    assert out.strip() == "Hello, World!"


def test_eval():
    out = rpp.eval("5+5;")
    assert out == 10.0
