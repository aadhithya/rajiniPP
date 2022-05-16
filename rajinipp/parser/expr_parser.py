# from loguru import logger

from ..ast.ops import UnarySub, UnarySum


class ExpressionParser:
    """parse all kinds of expressions."""

    def parse(self, pg):
        @pg.production(
            "expression : expression mathop expression", precedence="MATHOP"
        )
        def binary_arith_expr(p):
            # logger.debug("Parser --> expression")
            left = p[0]
            right = p[2]
            OpNode = p[1]

            return OpNode(left, right)

        @pg.production(
            "expression : expression logicalop expression",
            precedence="LOGICOP",
        )
        @pg.production(
            "logical_expression : expression logicalop expression",
            precedence="LOGICOP",
        )
        def binary_logical_op(p):
            left = p[0]
            right = p[2]
            OpNode = p[1]

            return OpNode(left, right)

        @pg.production("expression : SUB expression")
        @pg.production("expression : SUM expression")
        def unary_expr(p):
            if p[0].gettokentype() == "SUM":
                return UnarySum(p[1])
            if p[0].gettokentype() == "SUB":
                return UnarySub(p[1])
