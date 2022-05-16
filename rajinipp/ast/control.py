from ..__rajiniworld__ import __functions__, __vars__
from ..execptions import BreakException, ReturnException
from .base import Node, Word


class IfCondition(Node):
    def __init__(self, condition, value) -> None:
        super().__init__()
        self.condition = condition
        self.value = value

    def eval(self):
        if self.condition.eval():
            return self.value.eval()
        return


class IfElseCondition(Node):
    def __init__(self, condition, true_value, false_value) -> None:
        super().__init__()
        self.condition = condition
        self.true_value = true_value
        self.false_value = false_value

    def eval(self):
        if self.condition.eval():
            return self.true_value.eval()
        else:
            return self.false_value.eval()


class ForLoop(Node):
    def __init__(self, range_start, range_end, stmts) -> None:
        super().__init__()
        self.range_start = range_start
        self.range_end = range_end
        self.stmts = stmts

    def eval(self):
        # * we surround with try-catch block to support break command.
        try:
            st = int(self.range_start.eval())
            end = int(self.range_end.eval())
            for _ in range(st, end):
                self.stmts.eval()
        except BreakException:
            pass
        return


class WhileLoop(Node):
    def __init__(self, condition, stmts) -> None:
        super().__init__()
        self.condition = condition
        self.stmts = stmts

    def eval(self):
        # * we surround with try-catch block to support break command.
        try:
            while self.condition.eval():
                self.stmts.eval()
        except BreakException:
            pass
        return


class Break(Node):
    def __init__(self) -> None:
        super().__init__()

    def eval(self):
        raise BreakException(
            "BLACK SHEEP(break command) can be issued only inside loops!!"
        )


class FuncCall(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        return self.value.eval()


class FuncCallAssign(FuncCall):
    def __init__(self, var, value) -> None:
        super().__init__(value)
        self.var = var

    def eval(self):
        __vars__[self.var.name] = self.value.eval()
        return


class FuncWord(Word):
    def __init__(self, value) -> None:
        super().__init__(value)

    def eval(self):
        try:
            __functions__[self.value.value].eval()
        except ReturnException as ret_ex:
            return ret_ex.return_value.eval()


class Function(Node):
    def __init__(self, name, stmts) -> None:
        super().__init__()
        self._name = name
        self.stmts = stmts

    @property
    def name(self):
        return self._name.name

    def eval(self):
        __functions__[self.name] = self.stmts
        return


class FuncReturn(Node):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self):
        raise ReturnException(
            f"return triggered! Returning: {self.value.eval()}",
            self.value,
        )
