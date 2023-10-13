#!/usr/bin/env python3
import prompt
from random import choice, randrange as rr
from brain_games.logic import game_logic

game_rules = 'What is the result of the expression?'


def game_calc() -> tuple:
    oper = choice(("+", "-", "*"))
    num1, num2 = rr(51), rr(11) if oper == '*' else rr(51)
    match oper:
        case '+':
            true_answer = num1 + num2
        case '-':
            true_answer = num1 - num2
        case '*':
            true_answer = num1 * num2
    print(f'Question: {num1} {oper} {num2}')
    answer = prompt.string('Your answer: ')
    if answer.isdigit() or answer[1:].isdigit() and answer[0] == '-':
        answer = int(answer)
    return answer, true_answer


def main():
    game_logic(game_rules, game_calc)


if __name__ == '__main__':
    main()
