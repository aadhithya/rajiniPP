from ..execptions import BreakException
from .base import Node


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
