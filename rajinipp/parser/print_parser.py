# from loguru import logger

from ..ast.blocks import PrintBlock


class PrintParser:
    """parse print statements"""

    def parse(self, pg):
        @pg.production(
            "printexprs : printexprs expression", precedence="NOOP"
        )
        def print_exprs(p):
            # logger.debug("Parser --> print_exprs")
            return PrintBlock(p[0], p[1])

        @pg.production("printexprs : ")
        def printexprs_empty(p):
            # logger.debug("Parser --> print_empty")
            return PrintBlock()
