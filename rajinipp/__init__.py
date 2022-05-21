"""rajini++"""
from . import ast, lexer, parser, runner, utils

__all__ = ["parser", "ast", "lexer", "runner", "utils"]

__version__ = "0.3.1"
__version_str__ = (
    f"rajini++ v{__version__}."
    + "\nrajini++ is a programming language based on the iconic dialogues of super star Rajinikanth."
    + "\nCreated by Aadhithya Sankar(a.sankar@tum.de)."
)

rpp = runner.RppRunner()
