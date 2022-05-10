from typing import List

from loguru import logger
from rply import ParserGenerator

from ..ast.base import Assignment
from ..ast.blocks import MainBlock
from .atom_parser import AtomParser
from .expr_parser import ExpressionParser
from .print_parser import PrintParser
from .stmt_parser import StatementParser
from .var_parser import VariableParser


class Parser:
    def __init__(self, tokens: List[str]) -> None:
        self.pg = ParserGenerator(
            tokens=tokens,
            precedence=[
                ("left", ["NOOP"]),
                ("left", ["SUM", "SUB"]),
                ("left", ["MUL", "DIV", "MOD"]),
            ],
        )

        self.parsers = [
            StatementParser(),
            ExpressionParser(),
            PrintParser(),
            VariableParser(),
            AtomParser(),
        ]

    def parse(self):
        @self.pg.production("main : PGM_START statements PGM_END")
        def main(p):
            logger.debug("Parser --> main")
            return MainBlock(p[1])

        # * Add all other parsers.
        for parser in self.parsers:
            parser.parse(self.pg)

        @self.pg.error
        def error(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()