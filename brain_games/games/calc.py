import random
from brain_games.engine import game_engine
from brain_games.constants import (
    GAME_RULES_CALC,
    LIMIT_FOR_CALC as LIMIT,
    OPERATORS
)


def _get_expression() -> tuple:
    oper = random.choice(OPERATORS)
    num1, num2 = random.randrange(LIMIT), random.randrange(LIMIT)
    return num1, oper, num2


def _get_result_math_operation(num1, oper, num2):
    match oper:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2


def _prepare_game_data() -> tuple:
    expression = _get_expression()
    correct_answer = str(_get_result_math_operation(*expression))
    return expression, correct_answer


def run_game_calc():
    game_engine(GAME_RULES_CALC, _prepare_game_data)
