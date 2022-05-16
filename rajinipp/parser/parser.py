from typing import List

# from loguru import logger
from rply import ParserGenerator

from ..ast.base import Expression, Print
from ..ast.blocks import MainBlock, ProgramBlock
from .atom_parser import AtomParser
from .expr_parser import ExpressionParser
from .flow_parser import ConditionalParser, LoopParser
from .func_parser import FunctionParser
from .ops_parser import BinaryLogicalOpsParser, BinaryMathOpsParser
from .print_parser import PrintParser
from .stmt_parser import StatementParser
from .var_parser import VariableParser


class ParserBase:
    def __init__(self, tokens: List[str]) -> None:
        self.pg = ParserGenerator(
            tokens=tokens,
            precedence=[
                ("left", ["NOOP"]),
                ("left", ["LOGICOP"]),
                ("left", ["MATHOP"]),
                ("left", ["SUM", "SUB"]),
                ("left", ["MUL", "DIV", "MOD"]),
            ],
        )

        self.parsers = [
            StatementParser(),
            ExpressionParser(),
            BinaryMathOpsParser(),
            BinaryLogicalOpsParser(),
            PrintParser(),
            VariableParser(),
            AtomParser(),
        ]

    def parse(self):
        pass

    def init_parsers(self):
        """initialize other parsers"""
        # * Add all other parsers.
        for parser in self.parsers:
            parser.parse(self.pg)

        @self.pg.error
        def error(token):
            raise ValueError(token)

    def get_parser(self):
        """builds and returns parser"""
        return self.pg.build()


class ProgramParser(ParserBase):
    def __init__(self, tokens: List[str]) -> None:
        super().__init__(tokens)
        self.parsers += [
            ConditionalParser(),
            LoopParser(),
            FunctionParser(),
        ]

    def parse(self):
        @self.pg.production("program : functions main")
        def program(p):
            return ProgramBlock(p[0], p[1])

        @self.pg.production("main : PGM_START statements PGM_END")
        def main(p):
            # logger.debug("Parser --> main")
            return MainBlock(p[1])

        self.init_parsers()


class LineParser(ParserBase):
    def __init__(self, tokens: List[str]) -> None:
        super().__init__(tokens)

    def parse(self):
        @self.pg.production("statement : PRINT printexprs SEMI_COLON")
        def print_stmt(p):
            return Print(p[1])

        @self.pg.production("statement : expression SEMI_COLON")
        def expr_stms(p):
            return Expression(p[0])

        self.init_parsers()
