from rply import LexerGenerator
from .utils import read_yml


class Lexer:
    def __init__(self, token_yml: str = None) -> None:
        self._lexer = LexerGenerator()
        self._tokens = read_yml(token_yml)

    def __add_tokens(self):
        for token in self._tokens:
            self._lexer.add(token, r"{}".format(self._tokens[token]))

        # * ignore spaces
        self._lexer.ignore(r"\s+")

    def get_lexer(self):
        """builds and returns lexer."""
        self.__add_tokens()
        return self._lexer.build()
