from abc import ABC, abstractclassmethod

from ..__rajiniworld__ import __vars__


class Node(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.scope = "main"
        self._prev_scope = "main"

    @abstractclassmethod
    def eval(self):
        pass

    def set_scope(self, scope: str = "main"):
        self._prev_scope = self.scope
        self.scope = scope


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
        return __vars__[self.scope][self.name]


class Print(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def set_scope(self, scope: str = "main"):
        super().set_scope(scope)
        self.value.set_scope(scope)

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

    def __update_var_scope(self):
        if self.var.name in __vars__[self._prev_scope]:
            __vars__[self.scope][self.var.name] = __vars__[self._prev_scope][
                self.var.name
            ]
            _ = __vars__[self._prev_scope].pop(self.var.name, None)

    def set_scope(self, scope: str = "main"):
        super().set_scope(scope)
        # self.__update_var_scope()
        self.value.set_scope(scope)

    def eval(self):
        # * save just the variable values instead of the node.
        if self.scope not in __vars__:
            __vars__[self.scope] = {}
        __vars__[self.scope][self.var.name] = self.value.eval()
        return self.value.eval()


class VarAssign(Node):
    def __init__(self, var, value) -> None:
        super().__init__()
        self.var = var
        self.value = value

    def __update_var_scope(self):
        if self.var.name in __vars__[self._prev_scope]:
            __vars__[self.scope][self.var.name] = __vars__[self._prev_scope][
                self.var.name
            ]
            _ = __vars__[self._prev_scope].pop(self.var.name, None)

    def set_scope(self, scope: str = "main"):
        super().set_scope(scope)
        # self.__update_var_scope()
        self.value.set_scope(scope)

    def eval(self):
        if self.var.name not in __vars__[self.scope]:
            raise NameError(f"variable {self.var.name} does not exist.")
        __vars__[self.scope][self.var.name] = self.value.eval()


class Expression(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def set_scope(self, scope: str = "main"):
        super().set_scope(scope)
        self.value.set_scope(scope)

    def eval(self):
        return self.value.eval()
