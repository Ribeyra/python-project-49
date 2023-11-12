import random
from brain_games.engine import game_engine
from brain_games.constants import GAME_RULES_EVEN, LIMIT


def _is_even(num: int) -> bool:
    return num % 2 == 0


def _prepare_game_data() -> tuple:
    num = random.randrange(LIMIT)
    correct_answer = 'yes' if _is_even(num) else 'no'
    return num, correct_answer


def run_game_even():
    game_engine(GAME_RULES_EVEN, _prepare_game_data)
