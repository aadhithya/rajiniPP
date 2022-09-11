class BreakException(Exception):
    pass


class ReturnException(Exception):
    def __init__(self, message, return_value) -> None:
        super().__init__(message)
        self.return_value = return_value
