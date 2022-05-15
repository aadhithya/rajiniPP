from . import runner


def test_if(cond_code, capsys):
    runner.exec(cond_code)
    out, err = capsys.readouterr()
    assert "x ( 15.0 ) is equal to 15!" in out.strip()


def test_if_else(if_else_code, capsys):
    runner.exec(if_else_code)
    out, err = capsys.readouterr()
    assert "x ( 5.0 ) is less than 10!" in out.strip()
