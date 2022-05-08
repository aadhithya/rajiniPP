import os
import sys
from pathlib import Path

import typer
from loguru import logger

from .lexer import Lexer
from .parser import Parser
from .utils import read_yml

logger.remove()
logger.add(sys.stderr, level="INFO")


def main(file_path: str):
    with open(file_path, "r") as f:
        input_text = f.read()

    yml_path = os.path.join(Path(__file__).parent, "token.yml")
    # logger.info(yml_path)

    tokens_dict = read_yml(yml_path)

    lexer = Lexer(tokens_dict).get_lexer()
    tokens = lexer.lex(input_text)

    # for token in tokens:
    #     print(token)

    parser = Parser(list(tokens_dict.keys()))
    parser.parse()

    parser = parser.get_parser()

    parsed = parser.parse(tokens)

    parsed.eval()


if __name__ == "__main__":
    typer.run(main)
