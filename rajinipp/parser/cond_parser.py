from ..ast.control import IfCondition


class ConditionalParser:
    """parse conditional statements"""

    def parse(self, pg):
        @pg.production(
            "statement : IF_COND logical_expression L_BRACE statements R_BRACE END_BLOCK SEMI_COLON"
        )
        def if_stmt(p):
            return IfCondition(p[1], p[3])
