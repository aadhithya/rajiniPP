from ..ast.ops import (
    Div,
    LogicalEQ,
    LogicalGT,
    LogicalGTE,
    LogicalLT,
    LogicalLTE,
    LogicalNEQ,
    Mod,
    Mul,
    Sub,
    Sum,
)


class BinaryMathOpsParser:
    def parse(self, pg):
        @pg.production("mathop : SUM")
        def binary_sum(p):
            return Sum

        @pg.production("mathop : SUB")
        def binary_sub(p):
            return Sub

        @pg.production("mathop : MUL")
        def binary_mul(p):
            return Mul

        @pg.production("mathop : DIV")
        def binary_div(p):
            return Div

        @pg.production("mathop : MOD")
        def binary_mod(p):
            return Mod


class BinaryLogicalOpsParser:
    def parse(self, pg):
        @pg.production("logicalop : GT")
        def binary_gt(p):
            return LogicalGT

        @pg.production("logicalop : GTE")
        def binary_gte(p):
            return LogicalGTE

        @pg.production("logicalop : LT")
        def binary_lt(p):
            return LogicalLT

        @pg.production("logicalop : LTE")
        def binary_lte(p):
            return LogicalLTE

        @pg.production("logicalop : EQ")
        def binary_eq(p):
            return LogicalEQ

        @pg.production("logicalop : NEQ")
        def binary_neq(p):
            return LogicalNEQ
