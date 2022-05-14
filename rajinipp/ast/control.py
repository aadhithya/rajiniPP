from .base import Node


class IfCondition(Node):
    def __init__(self, condition, value) -> None:
        super().__init__()
        self.condition = condition
        self.value = value

    def eval(self):
        if self.condition:
            return self.value.eval()
        return
