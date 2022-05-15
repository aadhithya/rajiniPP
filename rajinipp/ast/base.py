from abc import ABC, abstractclassmethod

from ..__rajiniworld__ import __vars__


class Node(ABC):
    @abstractclassmethod
    def eval(self):
        pass


class Number(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        return float(self.value)


class Boolean(Node):
    def __init__(self, value) -> None:
        super().__init__()
        if value.value.lower() == "true":
            self.value = 1
        elif value.value.lower() == "false":
            self.value = 0

    def eval(self):
        return bool(self.value)


class String(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        return self.value.replace('"', "")


class Word(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    @property
    def name(self):
        return self.value.value

    def eval(self):
        return __vars__[self.name]


class Print(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        value = self.value.eval()
        if isinstance(value, list):
            print(*value)
        else:
            print(value)


class Statement(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        return self.value.eval()


class VarDeclare(Node):
    def __init__(self, var, value) -> None:
        super().__init__()
        self.var = var
        self.value = value

    def eval(self):
        # * save just the variable values instead of the node.
        __vars__[self.var.name] = self.value.eval()
        return self.value.eval()


class VarAssign(Node):
    def __init__(self, var, value) -> None:
        super().__init__()
        self.var = var
        self.value = value

    def eval(self):
        if self.var.name not in __vars__:
            raise NameError(f"variable {self.var.name} does not exist.")
        __vars__[self.var.name] = self.value.eval()


class Expression(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        return self.value.eval()
