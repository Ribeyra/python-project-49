import random
from brain_games.utils import get_random_num
from brain_games.engine import play_game
from brain_games.constants import GAME_RULE_PRIME, LIMITS


def is_prime(num: int) -> bool:
    for divisor in range(2, int(num ** (0.5)) + 1):
        if num % divisor == 0:
            return False
    return True


def generate_num_and_check_is_prime() -> tuple:

    def _cast_num_to_target_type(num, prime) -> int:
        while prime != is_prime(num):
            num += 1
        return num

    prime = random.choice([True, False])
    random_num = get_random_num(LIMITS[0], LIMITS[1])
    num = _cast_num_to_target_type(random_num, prime)
    prime_str = 'yes' if prime else 'no'
    return num, prime_str


def run_game_prime():
    play_game(GAME_RULE_PRIME, generate_num_and_check_is_prime)
