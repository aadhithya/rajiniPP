import pdb

from ..ast.control import ForLoop, IfCondition, IfElseCondition


class ConditionalParser:
    """parse conditional statements"""

    def parse(self, pg):
        @pg.production(
            "statement : IF_COND logical_expression L_BRACE statements R_BRACE END_BLOCK SEMI_COLON"
        )
        def if_stmt(p):
            return IfCondition(p[1], p[3])

        @pg.production(
            "statement : IF_COND logical_expression L_BRACE statements R_BRACE "
            + "ELSE_COND L_BRACE statements R_BRACE END_BLOCK SEMI_COLON"
        )
        def if_else_stmt(p):
            return IfElseCondition(p[1], p[3], p[7])


class LoopParser:
    """parse loops"""

    def parse(self, pg):
        @pg.production(
            "statement : FOR_START forvar FOR_RANGE_START forvar FOR_RANGE_END"
            + " L_BRACE statements R_BRACE END_BLOCK SEMI_COLON"
        )
        def for_loop(p):
            return ForLoop(p[1], p[3], p[6])
