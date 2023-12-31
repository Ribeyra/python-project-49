from brain_games.utils import get_random_num
from brain_games.engine import play_game
from brain_games.constants import GAME_RULE_GCD, LIMITS


def get_gcd(num1: int, num2: int) -> int:
    if num2 == 0:                        # Вариант бинарного алгоритма,
        return num1                      # предложенный ChatGPT
    return get_gcd(num2, num1 % num2)


def generate_nums_and_found_gcd() -> tuple:
    num1, num2 = get_random_num(LIMITS), get_random_num(LIMITS)
    correct_answer = str(get_gcd(num1, num2))
    nums_str = f'{num1} {num2}'
    return nums_str, correct_answer


def run_game_gcd():
    play_game(GAME_RULE_GCD, generate_nums_and_found_gcd)
