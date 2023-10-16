#!/usr/bin/env python3
from brain_games.logic import game_logic
from brain_games.games.prime import game_prime

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    game_logic(GAME_RULES, game_prime)


if __name__ == '__main__':
    main()
