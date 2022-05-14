from loguru import logger

from ..ast.base import Boolean, Expression, Number, Print, String, Word


class AtomParser:
    """parse all atomic components."""

    def parse(self, pg):
        @pg.production("expression : NUMBER")
        def number_expr(p):
            logger.debug("Parser --> number")
            return Number(p[0].value)

        @pg.production("expression : BOOL_TRUE")
        @pg.production("expression : BOOL_FALSE")
        def bool_expr(p):
            return Boolean(p[0])

        @pg.production("expression : STRING")
        def string_expr(p):
            logger.debug("Parser --> string")
            return String(p[0].value)

        @pg.production("expression : WORD")
        @pg.production("variable : WORD")
        def word_expr(p):
            return Word(p[0])