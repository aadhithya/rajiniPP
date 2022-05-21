from rajinipp import rpp


def test_if(cond_code, capsys):
    rpp.exec(cond_code)
    out, err = capsys.readouterr()
    assert "x ( 15.0 ) is equal to 15!" in out.strip()


def test_if_else(if_else_code, capsys):
    rpp.exec(if_else_code)
    out, err = capsys.readouterr()
    assert "x ( 5.0 ) is less than 10!" in out.strip()


def test_for_loop(for_loop_code, capsys):
    rpp.exec(for_loop_code)
    out, err = capsys.readouterr()
    assert "After loop: X = 14.0" in out.strip()


def test_while_loop(while_loop_code, capsys):
    rpp.exec(while_loop_code)
    out, err = capsys.readouterr()
    assert "breaking out of loop..." in out.strip()
