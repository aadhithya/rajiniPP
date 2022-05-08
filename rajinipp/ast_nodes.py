from abc import ABC, abstractclassmethod

from loguru import logger


class Node(ABC):
    @abstractclassmethod
    def eval(self):
        pass


class Number(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        return int(self.value)


class String(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        return self.value.replace('"', "")


class BinaryOp(Node):
    def __init__(self, left, right) -> None:
        super().__init__()
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Print(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        logger.debug(f"Print-value:{self.value.eval()}")
        print(self.value.eval())


class Statement(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        return self.value.eval()


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
