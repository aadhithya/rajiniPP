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
        return float(self.value)


class String(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        return self.value.replace('"', "")


class Print(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        # logger.debug(f"Print-value:{self.value.eval()}")
        print(self.value.eval())


class Statement(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        return self.value.eval()
