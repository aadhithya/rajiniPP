from loguru import logger

from ..ast.ops import Div, Mod, Mul, Sub, Sum, UnarySub, UnarySum


class ExpressionParser:
    """parse all kinds of expressions."""

    def parse(self, pg):
        @pg.production("expression : expression SUM expression")
        @pg.production("expression : expression SUB expression")
        @pg.production("expression : expression MUL expression")
        @pg.production("expression : expression DIV expression")
        @pg.production("expression : expression MOD expression")
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

        @pg.production("expression : SUB expression")
        @pg.production("expression : SUM expression")
        def unary_expr(p):
            if p[0].gettokentype() == "SUM":
                return UnarySum(p[1])
            if p[0].gettokentype() == "SUB":
                return UnarySub(p[1])
