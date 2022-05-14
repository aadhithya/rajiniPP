"""
# rajinipp python API.
The rejinipp api exposes the rajinipp interpreter
to python scripts.
"""

import os
import sys
from pathlib import Path

from loguru import logger

from .lexer import Lexer
from .parser.parser import Parser
from .utils import read_yml


def exec(code: str):
    logger.remove()
    logger.add(sys.stderr, level="ERROR")

    yml_path = os.path.join(Path(__file__).parent, "token.yml")

    tokens_dict = read_yml(yml_path)

    lexer = Lexer(tokens_dict).get_lexer()
    tokens = lexer.lex(code)

    parser = Parser(list(tokens_dict.keys()))
    parser.parse()

    parser = parser.get_parser()

    parsed_tokens = parser.parse(tokens)

    parsed_tokens.eval()
