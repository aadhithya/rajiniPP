import pdb
from abc import ABC, abstractclassmethod

from loguru import logger

from ..__rajiniworld__ import variables


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
        return variables[self.name].eval()


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


class Assignment(Node):
    def __init__(self, var, value) -> None:
        super().__init__()
        self.var = var
        self.value = value
        variables[var.name] = self

    def eval(self):
        return self.value.eval()


class Expression(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        return self.value.eval()
