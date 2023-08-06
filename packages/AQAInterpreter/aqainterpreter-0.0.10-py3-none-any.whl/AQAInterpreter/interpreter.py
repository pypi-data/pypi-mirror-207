from AQAInterpreter.tokens import *
from AQAInterpreter.scanner import *
from AQAInterpreter.errors import *
from AQAInterpreter.environment import SymbolTable
from abc import abstractmethod
import inspect

environment = SymbolTable()


class Expr:
    @abstractmethod
    def interpret(self) -> object:
        ...

    @abstractmethod
    def unparse(self) -> str:
        ...


class Stmt:
    @abstractmethod
    def interpret(self, output: list[str]) -> object:
        ...

    @abstractmethod
    def unparse(self) -> str:
        ...


@dataclass
class Literal(Expr):
    value: object

    def interpret(self):
        return self.value

    def unparse(self) -> str:
        return repr(self.value)


@dataclass
class Logical(Expr):
    left: Expr
    operator: Token
    right: Expr

    def interpret(self):
        left = self.left.interpret()
        right = self.right.interpret()

        if self.operator.type == OR:
            if left:
                return left
        else:
            # operator is AND
            if not left:
                return left

        return right

    def unparse(self) -> str:
        if self.operator.type == OR:
            return f"{self.left.unparse()} or {self.right.unparse()}"
        else:
            return f"{self.left.unparse()} and {self.right.unparse()}"


@dataclass
class Unary(Expr):
    operator: Token
    right: Expr

    def interpret(self) -> object:
        if (type := self.operator.type) == MINUS:
            return -self.right.interpret()  # type: ignore
        elif type == NOT:
            return not self.right.interpret()

    def unparse(self) -> str:
        if (type := self.operator.type) == MINUS:
            return f"- {self.right.interpret()}"
        elif type == NOT:
            return f"not({self.right.interpret()})"


@dataclass
class Binary(Expr):
    left: Expr
    operator: Token
    right: Expr

    def interpret(self) -> object:
        left = self.left.interpret()
        right = self.right.interpret()

        if (token_type := self.operator.type) == ADD:
            if (type(left), type(right)) in {(str, int), (int, str)}:
                return str(left) + str(right)
            else:
                return left + right  # type: ignore
        elif token_type == MINUS:
            return left - right  # type: ignore
        elif token_type == TIMES:
            return left * right  # type: ignore
        elif token_type == DIVIDE:
            return left / right  # type: ignore
        elif token_type == GREATER:
            return left > right  # type: ignore
        elif token_type == GREATER_EQUAL:
            return left >= right  # type: ignore
        elif token_type == LESS:
            return left < right  # type: ignore
        elif token_type == LESS_EQUAL:
            return left <= right  # type: ignore
        elif token_type == EQUAL:
            return left == right
        elif token_type == NOT_EQUAL:
            return left != right

    def unparse(self) -> str:
        left = self.left.unparse()
        right = self.right.unparse()

        if (token_type := self.operator.type) == ADD:
            return f"{left} + {right}"
        elif token_type == MINUS:
            return f"{left} - {right}"
        elif token_type == TIMES:
            return f"{left} * {right}"
        elif token_type == DIVIDE:
            return f"{left} / {right}"
        elif token_type == GREATER:
            return f"{left} > {right}"
        elif token_type == GREATER_EQUAL:
            return f"{left} >= {right}"
        elif token_type == LESS:
            return f"{left} < {right}"
        elif token_type == LESS_EQUAL:
            return f"{left} <= {right}"
        elif token_type == EQUAL:
            return f"{left} == {right}"
        elif token_type == NOT_EQUAL:
            return f"{left} != {right}"


@dataclass
class Grouping(Expr):
    expression: Expr

    def interpret(self):
        return self.expression.interpret()

    def unparse(self) -> str:
        return f"({self.expression.unparse()})"


@dataclass
class Variable(Expr):
    name: Token

    def interpret(self):
        return environment.get(self.name)

    def unparse(self):
        return self.name.lexeme


@dataclass
class Print(Stmt):
    expression: Expr

    def interpret(self, output: list[str]):
        output.append(str(self.expression.interpret()))

    def unparse(self) -> str:
        return f"print({self.expression.unparse()})\n"


@dataclass
class While(Stmt):
    condition: Expr
    body: list[Stmt]

    def interpret(self, output: list[str]) -> object:
        while self.condition.interpret():
            for stmt in self.body:
                stmt.interpret(output)

    def unparse(self) -> str:
        SEP = "    "
        return f"""while {self.condition.unparse()}:
    {SEP.join(stmt.unparse() for stmt in self.body)}"""


@dataclass
class If(Stmt):
    condition: Expr
    then_branch: list[Stmt]
    else_branch: list[Stmt]

    def interpret(self, output: list[str]):
        if self.condition.interpret():
            for stmt in self.then_branch:
                stmt.interpret(output)
        else:
            for stmt in self.else_branch:
                stmt.interpret(output)

    # fmt: off
    def unparse(self) -> str:
        SEP = "\t"
        out = inspect.cleandoc(f"""
            if {self.condition.unparse()}:
                {SEP.join(stmt.unparse() for stmt in self.then_branch)}
            """) + "\n"
        
        if len(self.else_branch) >= 1:
            out += inspect.cleandoc(f"""
            else:
                {SEP.join(stmt.unparse() for stmt in self.else_branch)}
            """) + "\n"

        return out
    # fmt: on


@dataclass
class Var(Stmt):
    name: Token
    initialiser: Expr

    def interpret(self, output: list[str]):
        value = self.initialiser.interpret()
        environment.define(self.name.lexeme, value)

    def unparse(self) -> str:
        return f"{self.name.lexeme} = {self.initialiser.unparse()}\n"
