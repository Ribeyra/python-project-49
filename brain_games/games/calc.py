import prompt
import random
from brain_games.logic import game_logic
from brain_games.constants import (
    GAME_RULES_CALC,
    LIMIT_FOR_CALC,
    LIMIT_AT_MULT
    )


def get_expression():
    """
    Получает случайное выражение. Первым шагом происходит случайный выбор
    математической операции. Затем случайным образом определяются опернады. В
    случае, если выбрано умножение, второй операнд ограничается 10 (мне кажется
    решать примеры типа 48 * 37 не лучшее развлечение).
    """
    oper = random.choice(("+", "-", "*"))
    num1 = random.randrange(LIMIT_FOR_CALC)
    num2 = (random.randrange(LIMIT_AT_MULT) if oper == '*' else
            random.randrange(LIMIT_FOR_CALC))
    return num1, oper, num2


def get_true_answer(num1, oper, num2):
    """
    В зависимости от операнда, определяется верный ответ.
    """
    match oper:
        case '+':
            true_answer = num1 + num2
        case '-':
            true_answer = num1 - num2
        case '*':
            true_answer = num1 * num2
    return true_answer


def game_calc() -> tuple:
    """
    Функция game_calc определяет логику игры "калькулятор". Верный ответ
    приводится к строке для полседующего сравнения с ответом пользователя.
    Функция возвращает пару ответ, верный_ответ
    """
    num1, oper, num2 = get_expression()
    true_answer = str(get_true_answer(num1, oper, num2))
    print(f'Question: {num1} {oper} {num2}')
    answer = prompt.string('Your answer: ')
    return answer, true_answer


def run_game_calc():
    game_logic(GAME_RULES_CALC, game_calc)
