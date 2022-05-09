from loguru import logger

from .base import Node


class UnaryOp(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value


class UnarySum(UnaryOp):
    def __init__(self, value) -> None:
        super().__init__(value)

    def eval(self):
        return float(self.value.eval())


class UnarySub(UnaryOp):
    def __init__(self, value) -> None:
        super().__init__(value)

    def eval(self):
        return float(-self.value.eval())


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


class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Mod(BinaryOp):
    def eval(self):
        return self.left.eval() % self.right.eval()
