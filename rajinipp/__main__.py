import os
from pathlib import Path

from loguru import logger

from .lexer import Lexer

if __name__ == "__main__":
    input_text = "print(4+2);"

    yml_path = os.path.join(Path(__file__).parent, "token.yml")
    logger.info(yml_path)

    lexer = Lexer(yml_path).get_lexer()

    tokens = lexer.lex(input_text)

    for token in tokens:
        print(token)
