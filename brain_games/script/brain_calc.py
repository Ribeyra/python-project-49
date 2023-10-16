#!/usr/bin/env python3
from brain_games.logic import game_logic
from brain_games.games.calc import game_calc

GAME_RULES = 'What is the result of the expression?'


def main():
    game_logic(GAME_RULES, game_calc)


if __name__ == '__main__':
    main()
