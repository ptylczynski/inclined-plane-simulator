from sympy import Symbol, SympifyError
from sympy.parsing.sympy_parser import parse_expr

from errors.mathError import MathError
from maths.function import Function


class InputMonoFunction(Function):
    """
    Implementation of Function generic class so it can be used with functions given by user
    Each expression should be given as string, which will be parsed by sympy
    """
    def __init__(self, expression: str):
        super().__init__()
        self.function_symbol: Symbol = Symbol('t')
        self.expression = parse_expr(expression)
        print(self.expression)

    def __repr__(self):
        return str(self.expression)

    def set_expression(self, function):
        self.expression = parse_expr(function)
        # print(self.expression)

    def get_expression(self):
        return self.expression

    def evaluate(self, arg):
        # print(arg)
        return float(self.expression.subs(self.function_symbol, arg))
