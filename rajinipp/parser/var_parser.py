# from loguru import logger

from ..ast.base import VarAssign, VarDeclare


class VariableParser:
    """parse statements regarding variables"""

    def parse(self, pg):
        @pg.production(
            "statement : START_DECLARE variable DECLARE expression SEMI_COLON"
        )
        @pg.production(
            "statement : START_DECLARE variable DECLARE_ALT expression SEMI_COLON"
        )
        def declare_var_expr(p):
            # logger.debug("VariableParser --> assign_stmt")
            return VarDeclare(p[1], p[3])

        @pg.production("statement : variable ASSIGN expression SEMI_COLON")
        # @pg.production(
        #     "statement : variable ASSIGN_ALT expression SEMI_COLON"
        # )
        def assign_var_expr(p):
            return VarAssign(p[0], p[2])
