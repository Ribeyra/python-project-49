#!/usr/bin/env python3
from brain_games.logic import game_logic
from brain_games.games.even import game_even

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    game_logic(GAME_RULES, game_even)


if __name__ == '__main__':
    main()
