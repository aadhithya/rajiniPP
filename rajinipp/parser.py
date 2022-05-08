from typing import List

from loguru import logger
from rply import ParserGenerator

from .ast_nodes import (
    MainBlock,
    Number,
    Print,
    Statement,
    StatementsBlock,
    String,
    Sub,
    Sum,
)


class Parser:
    def __init__(self, tokens: List[str]) -> None:
        self.pg = ParserGenerator(
            tokens=tokens, precedence=[("left", ["SUM", "SUB"])]
        )

    def parse(self):
        @self.pg.production("main : PGM_START statements PGM_END")
        def main(p):
            logger.debug("Parser --> main")
            return MainBlock(p[1])

        @self.pg.production("statements : statements statement")
        def statements(p):
            logger.debug("Parser --> statements")
            return StatementsBlock(p[0], p[1])

        @self.pg.production("statements : ")
        def statements_empty(p):
            logger.debug("Parser --> statements_empty")
            return StatementsBlock()

        @self.pg.production(
            "statement : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON"
        )
        def statement_print(p):
            logger.debug("Parser --> statement_print")
            return Print(p[2])

        @self.pg.production("expression : expression SUM expression")
        @self.pg.production("expression : expression SUB expression")
        def expression(p):
            logger.debug("Parser --> expression")
            left = p[0]
            right = p[2]
            op = p[1]

            if op.gettokentype() == "SUM":
                return Sum(left, right)
            if op.gettokentype() == "SUB":
                return Sub(left, right)

        @self.pg.production("expression : NUMBER")
        def number_expr(p):
            logger.debug("Parser --> number")
            return Number(p[0].value)

        @self.pg.production("expression : STRING")
        def string_expr(p):
            logger.debug("Parser --> string")
            return String(p[0].value)

        @self.pg.error
        def error(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
