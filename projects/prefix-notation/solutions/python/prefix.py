import itertools
import json
import operator
import re
import sys

TOKEN = "TOKEN"
INT = "INT"
VAR = "VAR"

PATTERN_INT = r"^\d+$"

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}


def classify_token(token):
    """
    Classifies the given string  `token` as an operator, integer or variable
    """
    if token in ("+", "-", "*", "/"):
        return TOKEN
    elif re.match(PATTERN_INT, token):
        return INT
    else:
        return VAR


def cartesian_ranges(variables):
    """
  Given a dict of type:
  
  """
    keys = variables.keys()
    value_ranges = [list(range(*variables[k])) for k in keys]
    for product in itertools.product(*value_ranges):
        yield dict((k, v) for k, v in zip(keys, product))


class Prefix(object):
    def __init__(self, expression, variables):
        self.raw = expression
        self.variables = variables

        # Initialise state
        self.reset_tokens()

    def reset_tokens(self):
        self.tokens = iter(self.raw.split())

    def resolve_token(self, token):
        classification = classify_token(token)
        if classification == TOKEN:
            return self.eval_prefix(token)
        elif classification == INT:
            return int(token)
        else:
            return self.variables[token]

    def eval_prefix(self, op):
        a = self.resolve_token(next(self.tokens))
        b = self.resolve_token(next(self.tokens))
        return OPERATORS[op](a, b)

    def eval(self):
        return self.eval_prefix(next(self.tokens))


# Complete the evaluate_expression function below.
def max_result_expression(expression, variables):
    """
    Evaluates the prefix expression and calculates the maximum result
    for the given variable ranges.

    Arguments:
      expression (str): the prefix expression to evaluate.
      variables (dict): all the variables in the expression are the keys
          of this dictionary and their values are tuples `(min, max)` that
          define a range (the upper bound `max` is not included).
          
    Returns:
        int or None: the maximum result of the expression for any combination of the accepted
            values. If the expression is invalid, it will return `None`.
    """
    # print(f"Evaluating '{expression}'")
    variable_combinations = cartesian_ranges(variables)

    current_max = None
    for comb in variable_combinations:
        prefix = Prefix(expression, comb)
        ans = prefix.eval()
        # print(f"- Evaluated '{comb}' => {ans}")
        if current_max is None or ans > current_max:
            current_max = ans

    return current_max


if __name__ == "__main__":
    notation = next(sys.stdin)
    variables = json.loads(next(sys.stdin))
    print(max_result_expression(notation, variables))
