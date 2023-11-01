import random
from brain_games.engine import game_engine
from brain_games.constants import (
    GAME_RULES_PROGRESSION,
    LEN_ROW_LIMITS,
    START_LIMIT,
    STEP_LIMITS
)


def _get_progression() -> list:
    """
    Возвращает прогрессию случайной длинны в диапазоне LEN_ROW_LIMITS, с шагом
    в диапазоне STEP_LIMITS, с началом в диапазоне START_LIMIT.
    """
    step = random.randrange(STEP_LIMITS[0], STEP_LIMITS[1])
    len_row = random.randrange(LEN_ROW_LIMITS[0], LEN_ROW_LIMITS[1])
    start = random.randrange(START_LIMIT[0], START_LIMIT[1])
    row = [start]
    while len(row) < len_row:
        row.append(row[-1] + step)
    return row


def _game_progression() -> tuple:
    """
    Функция game_progression определяет логику игры «Арифметическая прогрессия»
    Функция get_progression возвращает случайную прогрессию. Далее определяем
    индекс числа, которое будет загадано, предусмотрев, что таким индексом не
    будет первое и последнее число ряда. Число под выбранным индеском,
    сохраняем в правильном ответе. Заменяем в ряду число под выбранным индексом
    на '..'. Функция возвращает значение для вопроса и верный_ответ
    """
    row = _get_progression()
    secret_index = random.randrange(1, len(row) - 1)
    correct_answer = str(row[secret_index])
    row[secret_index] = '..'
    return row, correct_answer


def run_game_progression():
    """
    Запускает игру
    """
    game_engine(GAME_RULES_PROGRESSION, _game_progression)
