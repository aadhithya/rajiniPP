# from loguru import logger

from .base import Node, Statement


class PrintBlock(Node):
    def __init__(self, exprs=None, value=None) -> None:
        super().__init__()
        self.exprs = exprs
        self.value = value

    def eval(self):
        if self.exprs:
            return self.exprs.eval() + [self.value.eval()]
        return []


class StatementsBlock(Node):
    def __init__(self, statements=None, statement: Statement = None) -> None:
        super().__init__()
        self.statements = statements
        self.statement = statement

    def eval(self):
        if self.statements:
            return self.statements.eval() + [self.statement.eval()]
        return []

    def get_list(self):
        if self.statements:
            return self.statements.get_list + [self.statement]
        return []


class MainBlock(Node):
    def __init__(self, statements: StatementsBlock) -> None:
        super().__init__()
        self.statements = statements

    def eval(self):
        return self.statements.eval()


class FunctionsBlock(Node):
    def __init__(self, functions=None, function=None) -> None:
        super().__init__()
        self.functions = functions
        self.function = function

    def eval(self):
        if self.functions:
            return self.functions.eval() + [self.function.eval()]
        return []


class ProgramBlock(Node):
    def __init__(self, functions, main) -> None:
        super().__init__()
        self.functions = functions
        self.main = main

    def eval(self):
        return self.functions.eval() + [self.main.eval()]
