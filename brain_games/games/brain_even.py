#!/usr/bin/env python3
import prompt
from random import randrange as rr
from brain_games.logic import game_logic

game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_even() -> tuple:
    """
    Функция game_even определяет логику игры "проверка на четность".
    Первым шагом генерируется случайное число, затем определяется верный ответ,
    после чего у пользователя запрашивается его вариант. Функция возвращает
    пару ответ, верный_ответ
    """
    limit = 101
    num = rr(limit)
    true_answer = 'no' if num % 2 else 'yes'   # alt ('yes', 'no')[num % 2]
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ').lower()
    return answer, true_answer


def main():
    game_logic(game_rules, game_even)


if __name__ == '__main__':
    main()
