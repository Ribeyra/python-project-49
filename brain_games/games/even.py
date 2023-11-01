import random
from brain_games.engine import game_engine
from brain_games.constants import GAME_RULES_EVEN, LIMIT


def _game_even() -> tuple:
    """
    Функция game_even определяет логику игры "проверка на четность".
    Первым шагом генерируется случайное число, затем определяется верный ответ.
    Функция возвращает значение для вопроса и верный_ответ
    """
    num = random.randrange(LIMIT)
    correct_answer = 'no' if num % 2 else 'yes'   # alt ('yes', 'no')[num % 2]
    return num, correct_answer


def run_game_even():
    """
    Запускает игру
    """
    game_engine(GAME_RULES_EVEN, _game_even)
