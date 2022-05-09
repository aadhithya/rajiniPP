from typing import List

from loguru import logger
from rply import ParserGenerator

from .ast.base import Assignment, Expression, Number, Print, String, Word
from .ast.blocks import MainBlock, PrintBlock, StatementsBlock
from .ast.ops import Div, Mod, Mul, Sub, Sum, UnarySub, UnarySum


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

    def parse(self):
        @self.pg.production("main : PGM_START statements PGM_END")
        def main(p):
            # logger.debug("Parser --> main")
            return MainBlock(p[1])

        @self.pg.production("statements : statements statement")
        def statements(p):
            # logger.debug("Parser --> statements")
            return StatementsBlock(p[0], p[1])

        @self.pg.production("statements : ")
        def statements_empty(p):
            logger.debug("Parser --> statements_empty")
            return StatementsBlock()

        @self.pg.production("statement : PRINT printexprs SEMI_COLON")
        def statement_print(p):
            logger.debug("Parser --> statement_print")
            return Print(p[1])

        # @self.pg.production("printexprs : printexprs COMMA printexprs")
        @self.pg.production(
            "printexprs : printexprs expression", precedence="NOOP"
        )
        def print_exprs(p):
            logger.debug("Parser --> print_exprs")
            return PrintBlock(p[0], p[1])

        @self.pg.production("printexprs : ")
        def printexprs_empty(p):
            logger.debug("Parser --> print_empty")
            return PrintBlock()

        @self.pg.production("expression : expression SUM expression")
        @self.pg.production("expression : expression SUB expression")
        @self.pg.production("expression : expression MUL expression")
        @self.pg.production("expression : expression DIV expression")
        @self.pg.production("expression : expression MOD expression")
        def binary_expr(p):
            logger.debug("Parser --> expression")
            left = p[0]
            right = p[2]
            op = p[1]

            if op.gettokentype() == "SUM":
                return Sum(left, right)
            if op.gettokentype() == "SUB":
                return Sub(left, right)
            if op.gettokentype() == "MUL":
                return Mul(left, right)
            if op.gettokentype() == "DIV":
                return Div(left, right)
            if op.gettokentype() == "MOD":
                return Mod(left, right)

        @self.pg.production("expression : SUB expression")
        @self.pg.production("expression : SUM expression")
        def unary_expr(p):
            if p[0].gettokentype() == "SUM":
                return UnarySum(p[1])
            if p[0].gettokentype() == "SUB":
                return UnarySub(p[1])

        @self.pg.production(
            "statement : START_ASSIGN variable ASSIGN expression SEMI_COLON"
        )
        @self.pg.production(
            "statement : START_ASSIGN variable EQUALS expression SEMI_COLON"
        )
        def assign_stmt(p):
            return Assignment(p[1], p[3])

        @self.pg.production("expression : NUMBER")
        def number_expr(p):
            logger.debug("Parser --> number")
            return Number(p[0].value)

        @self.pg.production("expression : STRING")
        def string_expr(p):
            logger.debug("Parser --> string")
            return String(p[0].value)

        @self.pg.production("expression : WORD")
        @self.pg.production("variable : WORD")
        def word_expr(p):
            return Word(p[0])

        @self.pg.error
        def error(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
