from sympy import Symbol, SympifyError
from sympy.parsing.sympy_parser import parse_expr

from errors.mathError import MathError


class Function:
    def __init__(self):
        self.last_arg = None
        self.cashed = None

    def evaluate(self, arg):
        raise NotImplemented()

    def __getitem__(self, item) -> float:
        try:
            if self.last_arg is None or item != self.last_arg:
                self.cashed = self.evaluate(item)
                self.last_arg = item
            return self.cashed

        except SympifyError:
            raise MathError("Unrecognized symbols or tokens")

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass
