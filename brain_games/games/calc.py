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
    num1, num2 = get_random_num(LIMIT), get_random_num(LIMIT)
    return oper, num1, num2


def get_expression() -> str:
    oper, num1, num2 = get_random_operator_and_nums()
    return ' '.join((str(num1), oper, str(num2)))


def get_result_math_operation(expression: str):
    num1, oper, num2 = expression.split()
    match oper:
        case '+':
            return int(num1) + int(num2)
        case '-':
            return int(num1) - int(num2)
        case '*':
            return int(num1) * int(num2)


def generate_expression_and_result() -> tuple:
    expression = get_expression()
    result = str(get_result_math_operation(expression))
    return expression, result


def run_game_calc():
    play_game(GAME_RULE_CALC, generate_expression_and_result)
