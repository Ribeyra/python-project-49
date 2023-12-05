from brain_games.utils import get_random_num
from brain_games.engine import play_game
from brain_games.constants import GAME_RULE_EVEN, LIMIT


def is_even(num: int) -> bool:
    return num % 2 == 0


def generate_num_and_check_is_even() -> tuple:
    num = get_random_num([LIMIT])
    even = 'yes' if is_even(num) else 'no'
    return num, even


def run_game_even():
    play_game(GAME_RULE_EVEN, generate_num_and_check_is_even)
