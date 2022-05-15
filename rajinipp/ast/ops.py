from .base import Node


class UnaryOpBase(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value


class UnarySum(UnaryOpBase):
    def __init__(self, value) -> None:
        super().__init__(value)

    def eval(self):
        return float(self.value.eval())


class UnarySub(UnaryOpBase):
    def __init__(self, value) -> None:
        super().__init__(value)

    def eval(self):
        return float(-self.value.eval())


class BinaryOpBase(Node):
    def __init__(self, left, right) -> None:
        super().__init__()
        self.left = left
        self.right = right


class Sum(BinaryOpBase):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOpBase):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Mul(BinaryOpBase):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOpBase):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Mod(BinaryOpBase):
    def eval(self):
        return self.left.eval() % self.right.eval()


class LogicalGT(BinaryOpBase):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self):
        return self.left.eval() > self.right.eval()


class LogicalGTE(BinaryOpBase):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self):
        return self.left.eval() >= self.right.eval()


class LogicalLT(BinaryOpBase):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self):
        return self.left.eval() < self.right.eval()


class LogicalLTE(BinaryOpBase):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self):
        return self.left.eval() <= self.right.eval()


class LogicalEQ(BinaryOpBase):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self):
        return self.left.eval() == self.right.eval()


class LogicalNEQ(BinaryOpBase):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self):
        return self.left.eval() != self.right.eval()
