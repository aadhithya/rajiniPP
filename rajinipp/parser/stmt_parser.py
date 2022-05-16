# from loguru import logger

from ..ast.base import Print
from ..ast.blocks import StatementsBlock


class StatementParser:
    """parse all kinds of statements."""

    def parse(self, pg):
        @pg.production("statements : statements statement")
        def statements(p):
            # logger.debug("Parser --> statements")
            return StatementsBlock(p[0], p[1])

        @pg.production("statements : ")
        def statements_empty(p):
            # logger.debug("Parser --> statements_empty")
            # logger.debug(p)
            return StatementsBlock()

        @pg.production("statement : PRINT printexprs SEMI_COLON")
        def statement_print(p):
            # logger.debug("Parser --> statement_print")
            return Print(p[1])
