#!/usr/bin/env python3
import prompt
from random import randrange as rr
from brain_games.logic import game_logic

game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_even() -> tuple:
    num = rr(101)    # generate random number in limit 101
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ').lower()
    true_answer = 'no' if num % 2 else 'yes'   # alt ('yes', 'no')[num % 2]
    return answer, true_answer


def main():
    game_logic(game_rules, game_even)


if __name__ == '__main__':
    main()
