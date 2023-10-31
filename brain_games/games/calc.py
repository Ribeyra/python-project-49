import prompt
import random
from brain_games.engine import game_engine
from brain_games.constants import (
    GAME_RULES_CALC,
    LIMIT_FOR_CALC as LIMIT
)


def _get_expression():
    """
    Возвращает случайное математическое выражение.
    """
    oper = random.choice(("+", "-", "*"))
    num1, num2 = random.randrange(LIMIT), random.randrange(LIMIT)
    return oper, num1, num2


"""
В случае, если выбрано умножение, второй операнд ограничается 10 (мне кажется
решать примеры типа 48 * 37 не лучшее развлечение).
num2 = (random.randrange(LIMIT_AT_MULT) if oper == '*' else
        random.randrange(LIMIT_FOR_CALC))
"""


def _get_correct_answer(oper, num1, num2):
    """
    В качестве аргументов принимает мат операцию и операнды.
    Возвращает верный ответ
    """
    match oper:
        case '+':
            correct_answer = num1 + num2
        case '-':
            correct_answer = num1 - num2
        case '*':
            correct_answer = num1 * num2
    return correct_answer


def _game_calc() -> tuple:
    """
    Функция game_calc определяет логику игры "калькулятор". Верный ответ
    приводится к строке для последующего сравнения с ответом пользователя.
    Функция возвращает пару ответ, верный_ответ
    """
    oper, num1, num2 = _get_expression()
    correct_answer = str(_get_correct_answer(oper, num1, num2))
    print(f'Question: {num1} {oper} {num2}')
    answer = prompt.string('Your answer: ')
    return answer, correct_answer


def run_game_calc():
    """
    Запускает игру
    """
    game_engine(GAME_RULES_CALC, _game_calc)
