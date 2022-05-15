"""
# rajinipp python runner.
The rajinipp runner exposes the rajinipp interpreter
to python scripts.
"""

import os
import sys
from pathlib import Path

from loguru import logger

from .lexer import Lexer
from .parser.parser import Parser
from .utils import read_yml


class RppRunner:
    """
    The RppRunner handles the execution of rajini++ code.
    """

    def __init__(self) -> None:
        yml_path = os.path.join(Path(__file__).parent, "token.yml")
        self.tokens_dict = read_yml(yml_path)

    def tokenize(self, code: str):
        """
        tokenize tokenizes the input code.

        Args:
            code (str): the rajini++ code to tokenize.

        Returns:
            LexerStream: a generator of the tokens.
        """
        lexer = Lexer(self.tokens_dict).get_lexer()
        tokens = lexer.lex(code)
        return tokens

    def exec(self, code: str, log_level: str = "ERROR"):
        """
        exec executes a copmplete rajini++ program.

        Args:
            code (str): the rajini++ program to execute.
            log_level (str, optional): log level. Defaults to "ERROR".
        """
        logger.remove()
        logger.add(sys.stderr, level=log_level)

        parser = Parser(list(self.tokens_dict.keys()))
        parser.parse()

        parser = parser.get_parser()

        parsed_tokens = parser.parse(self.tokenize(code))

        parsed_tokens.eval()
