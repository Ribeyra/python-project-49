import random
from brain_games.engine import game_engine
from brain_games.constants import (
    GAME_RULES_PROGRESSION,
    LEN_ROW_LIMITS,
    START_LIMIT,
    STEP_LIMITS
)


def _get_progression() -> list:
    step = random.randint(STEP_LIMITS[0], STEP_LIMITS[1])
    len_row = random.randint(LEN_ROW_LIMITS[0], LEN_ROW_LIMITS[1])
    start = random.randint(START_LIMIT[0], START_LIMIT[1])
    row = [start]
    while len(row) < len_row:
        row.append(row[-1] + step)
    return row


def _prepare_game_data() -> tuple:
    row = _get_progression()
    secret_index = random.randrange(1, len(row) - 1)
    correct_answer = str(row[secret_index])
    row[secret_index] = '..'
    return row, correct_answer


def run_game_progression():
    game_engine(GAME_RULES_PROGRESSION, _prepare_game_data)
