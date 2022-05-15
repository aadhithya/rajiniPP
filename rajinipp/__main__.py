from typer import Typer

from . import __version_str__
from .runner import RppRunner

app = Typer()
runner = RppRunner()


@app.command()
def version():
    """prints version and exits."""
    print(__version_str__)


@app.command()
def tokenize(file_path: str):
    """prints the tokens from the program."""
    with open(file_path, "r") as f:
        code_str = f.read()
    tokens = runner.tokenize(code=code_str)
    for token in tokens:
        print(token)


@app.command()
def run(file_path: str, debug: bool = False):
    """executes a rajini++ program."""
    level = "DEBUG" if debug else "INFO"
    with open(file_path, "r") as f:
        code_str = f.read()
    runner.exec(code=code_str, log_level=level)


@app.callback()
def main():
    """
    rajini++(rajinipp) is a hobby programming language based on the iconic dialogues of super star Rajinikanth.
    """


if __name__ == "__main__":
    app()
