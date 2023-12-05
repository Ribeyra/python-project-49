import random
from brain_games.utils import get_random_num
from brain_games.engine import play_game
from brain_games.constants import (
    GAME_RULE_CALC,
    LIMIT_FOR_CALC as LIMIT,
    OPERATORS
)


def get_random_operator_and_nums() -> tuple:
    oper = random.choice(OPERATORS)
    num1, num2 = get_random_num([LIMIT]), get_random_num([LIMIT])
    return oper, num1, num2


def get_result_math_operation(oper: str, num1: int, num2: int):
    match oper:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2


def generate_expression_and_result() -> tuple:
    oper, num1, num2 = get_random_operator_and_nums()
    expression = ' '.join((str(num1), oper, str(num2)))
    result = str(get_result_math_operation(oper, num1, num2))
    return expression, result


def run_game_calc():
    play_game(GAME_RULE_CALC, generate_expression_and_result)
