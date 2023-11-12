import random
from brain_games.engine import game_engine
from brain_games.constants import GAME_RULES_PRIME, LIMITS


def _is_prime(num: int) -> bool:
    for divisor in range(2, int(num ** (0.5)) + 1):
        if num % divisor == 0:
            return False
    return True


def _prepare_game_data() -> tuple:
    prime_num = random.choice([True, False])
    num = random.randint(LIMITS[0], LIMITS[1])
    while prime_num != _is_prime(num):
        num += 1
    correct_answer = 'yes' if prime_num else 'no'
    return num, correct_answer


def run_game_prime():
    game_engine(GAME_RULES_PRIME, _prepare_game_data)
