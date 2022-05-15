from munch import Munch
from rply import LexerGenerator


class Lexer:
    def __init__(self, tokens: Munch = None) -> None:
        self._lexer = LexerGenerator()
        self._tokens = tokens

    def __add_tokens(self):
        for token in self._tokens:
            self._lexer.add(token, r"{}".format(self._tokens[token]))

        # * ignore spaces
        self._lexer.ignore(r"\s+")
        self._lexer.ignore(r"!!.*\n")

    def get_lexer(self):
        """builds and returns lexer."""
        self.__add_tokens()
        return self._lexer.build()
