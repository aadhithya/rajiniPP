import os
import sys
from pathlib import Path

from loguru import logger
from typer import Typer

from . import __version_str__
from .lexer import Lexer
from .parser.parser import Parser
from .utils import read_yml

app = Typer()


@app.command()
def version():
    """prints version and exits."""
    print(__version_str__)


@app.command()
def tokenize(file_path: str):
    """prints the tokens from the program."""
    with open(file_path, "r") as f:
        input_text = f.read()

    yml_path = os.path.join(Path(__file__).parent, "token.yml")

    tokens_dict = read_yml(yml_path)

    lexer = Lexer(tokens_dict).get_lexer()
    tokens = lexer.lex(input_text)

    for token in tokens:
        print(token)


@app.command()
def run(file_path: str, debug: bool = False):
    """executes a rajini++ program."""

    level = "DEBUG" if debug else "INFO"
    logger.remove()
    logger.add(sys.stderr, level=level)

    with open(file_path, "r") as f:
        input_text = f.read()

    yml_path = os.path.join(Path(__file__).parent, "token.yml")

    tokens_dict = read_yml(yml_path)

    lexer = Lexer(tokens_dict).get_lexer()
    tokens = lexer.lex(input_text)

    parser = Parser(list(tokens_dict.keys()))
    parser.parse()

    parser = parser.get_parser()

    parsed = parser.parse(tokens)

    parsed.eval()


@app.callback()
def main():
    """
    rajini++(rajinipp) is a hobby programming language based on the iconic dialogues of super star Rajinikanth.
    """


if __name__ == "__main__":
    app()
