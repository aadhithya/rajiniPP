from loguru import logger

from ..ast.base import Assignment


class VariableParser:
    """parse statements regarding variables"""

    def parse(self, pg):
        @pg.production(
            "statement : START_ASSIGN variable ASSIGN expression SEMI_COLON"
        )
        @pg.production(
            "statement : START_ASSIGN variable EQUALS expression SEMI_COLON"
        )
        def assign_stmt(p):
            logger.debug("VariableParser --> assign_stmt")
            return Assignment(p[1], p[3])
