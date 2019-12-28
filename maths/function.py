from sympy import Symbol, SympifyError
from sympy.parsing.sympy_parser import parse_expr

from errors.mathError import MathError


class Function:
    """
    Generic class for functions.
    Each functions should work as indexed data structure.
    Calling function[arg] should return value of function in place arg
    """
    def __init__(self):
        self.last_arg = None
        self.cashed = None

    def evaluate(self, arg):
        """
        Function called by __getitem__ to receive function value
        :param arg: place to calculate value
        :return: function value
        """
        raise NotImplemented()

    def __getitem__(self, item) -> float:
        """
        __getitem__ should each time check if value is not calculated for given argument.
        If so happen cashed value ought to be returned
        :param item: argument of function
        :return: value of function
        """
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
