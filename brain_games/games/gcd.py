import random
from brain_games.engine import game_engine
from brain_games.constants import GAME_RULES_GCD, LIMITS, NUMS_AMOUNT


def _get_gcd(num1: int, num2: int) -> int:
    if num2 == 0:                        # Вариант бинарного алгоритма,
        return num1                      # предложенный ChatGPT
    return _get_gcd(num2, num1 % num2)


def _prepare_game_data() -> tuple:
    nums = [random.randint(LIMITS[0], LIMITS[1]) for _ in range(NUMS_AMOUNT)]
    correct_answer = str(_get_gcd(*nums))
    return nums, correct_answer


def run_game_gcd():
    game_engine(GAME_RULES_GCD, _prepare_game_data)
