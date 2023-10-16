#!/usr/bin/env python3
from brain_games.logic import game_logic
from brain_games.games.progression import game_progression

GAME_RULES = 'What number is missing in the progression?'


def main():
    game_logic(GAME_RULES, game_progression)


if __name__ == '__main__':
    main()
