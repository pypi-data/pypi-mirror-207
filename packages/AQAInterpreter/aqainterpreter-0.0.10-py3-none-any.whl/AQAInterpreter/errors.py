from AQAInterpreter.tokens import *
from dataclasses import dataclass


@dataclass
class AQARuntimeError(RuntimeError):
    token: Token
    message: str


class AQAParseError(RuntimeError):
    token: Token
    message: str


def report(line: str, where: str, message: str, output: list[str]):
    output.append(f"[{line}] Error '{where}': {message}")


def error(token: Token | int, message: str, output: list[str]):
    if isinstance(token, Token):
        line = "end of file" if token.type == EOF else f"line {token.line}"
        where = "end of line" if token.type == NEWLINE else token.lexeme
        report(line, where, message, output)
    else:
        report("line {token}", "", message, output)

