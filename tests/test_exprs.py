from rajinipp import rpp


def test_conditional_exprs(cond_code, capsys):
    rpp.exec(cond_code)
    out, err = capsys.readouterr()
    assert "x ( 15.0 ) is equal to 15!" in out.strip()


def test_logical_exprs(logic_code, capsys):
    rpp.exec(logic_code)
    out, err = capsys.readouterr()
    assert "x != b:  True" in out.strip()


def test_math_exprs(math_code, capsys):
    rpp.exec(math_code)
    out, err = capsys.readouterr()
    assert "modvar =  1.0" in out.strip()
