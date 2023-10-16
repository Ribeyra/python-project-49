#!/usr/bin/env python3
from brain_games.logic import game_logic
from brain_games.games.gcd import game_gcd

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def main():
    game_logic(GAME_RULES, game_gcd)


if __name__ == '__main__':
    main()
