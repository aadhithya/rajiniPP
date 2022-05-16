from . import runner


def test_function(fn_code, capsys):
    runner.exec(fn_code)
    out, err = capsys.readouterr()
    assert "Hello from myfunc_one!" in out.strip()


def test_function_return(fn_return_code, capsys):
    runner.exec(fn_return_code)
    out, err = capsys.readouterr()
    assert "Value returned from myfunc_one: 100.0" in out.strip()
