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
