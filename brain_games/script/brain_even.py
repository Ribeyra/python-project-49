#!/usr/bin/env python3
import prompt
from random import randrange as rr
from ..cli import welcome_user


def verify_answer(num: int) -> bool:
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ').lower()
    true_answer = 'no' if num % 2 else 'yes'   # alt ('yes', 'no')[num % 2]
    if answer == true_answer:
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{true_answer}'")
        return False


def even_game() -> bool:
    for _ in range(3):
        random_num = rr(101)    # generate random number in limit 101
        if verify_answer(random_num):
            print('Correct!')
        else:
            return False
    else:
        return True


def main():
    text = 'Welcome to the Brain Games!'
    print(text)
    name = welcome_user()
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    if even_game():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
