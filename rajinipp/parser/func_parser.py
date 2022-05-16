from loguru import logger

from ..ast.blocks import FunctionsBlock
from ..ast.control import FuncCall, FuncCallAssign, FuncReturn, Function


class FunctionParser:
    """parse functions"""

    def parse(self, pg):
        @pg.production("functions : functions function")
        def functions(p):
            return FunctionsBlock(p[0], p[1])

        @pg.production("functions : ")
        def empty_function(p):
            return FunctionsBlock()

        @pg.production(
            "function : FUNC_DECLARE func_name statements END_FUNC"
        )
        def parse_function_no_args(p):
            logger.debug("Parse Function")
            return Function(p[1], p[2])

        @pg.production("statement : FUNC_RETURN expression SEMI_COLON")
        def return_stmt(p):
            return FuncReturn(p[1])

        @pg.production("statement : FUNC_CALL func_name SEMI_COLON")
        def func_call(p):
            logger.debug("Func Call")
            return FuncCall(p[1])

        @pg.production("statement : variable FUNC_CALL func_name SEMI_COLON")
        def func_call_assign(p):
            logger.debug("Func Assign")
            return FuncCallAssign(p[0], p[2])
