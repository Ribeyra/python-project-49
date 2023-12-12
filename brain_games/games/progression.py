from brain_games.utils import get_random_num
from brain_games.engine import play_game
from brain_games.constants import (
    GAME_RULE_PROGRESSION,
    LEN_ROW_LIMITS,
    START_LIMIT,
    STEP_LIMITS
)


def get_random_len_start_step() -> tuple:
    len_row = get_random_num(LEN_ROW_LIMITS)
    start = get_random_num(START_LIMIT)
    step = get_random_num(STEP_LIMITS)
    step = step if step else len_row    # exclude the case where the step is 0
    return len_row, start, step


def get_progression(len_row: int, start: int, step: int) -> list:
    progression = [start + i * step for i in range(len_row)]
    return progression


def generate_progression_and_secret_value() -> tuple:
    len_row, start, step = get_random_len_start_step()
    progression = get_progression(len_row, start, step)
    secret_index = get_random_num([1, len(progression) - 2])
    secret_value = str(progression[secret_index])
    progression[secret_index] = '..'
    progression_str = ' '.join(map(str, progression))
    return progression_str, secret_value


def run_game_progression():
    play_game(GAME_RULE_PROGRESSION, generate_progression_and_secret_value)
