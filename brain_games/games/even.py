import prompt
import random
from brain_games.logic import game_logic
from brain_games.constants import GAME_RULES_EVEN, LIMIT


def game_even() -> tuple:
    """
    Функция game_even определяет логику игры "проверка на четность". Первым
    шагом генерируется случайное число, затем определяется верный ответ,
    после чего у пользователя запрашивается его вариант. Функция возвращает
    пару ответ, верный_ответ
    """
    num = random.randrange(LIMIT)
    true_answer = 'no' if num % 2 else 'yes'   # alt ('yes', 'no')[num % 2]
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ').lower()
    return answer, true_answer


def run_game_even():
    game_logic(GAME_RULES_EVEN, game_even)
