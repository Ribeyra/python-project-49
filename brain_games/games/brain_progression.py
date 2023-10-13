#!/usr/bin/env python3
import prompt
from random import randrange as rr
from brain_games.logic import game_logic

game_rules = 'What number is missing in the progression?'


def game_progression() -> tuple:
    """
    Функция game_progression определяет логику игры «Арифметическая прогрессия»
    Вначале определяем шаг прогрессии, затем длину ряда, затем первое число.
    Затем собираем ряд, добавляем в список первое число, затем определнное
    кол-во чисел с нажным шагом от предыдущего числа. Далее определяем индекс
    числа, которое будет загадано, предусмострев, что таким индексом не будет
    первое и последнее число ряда. Число под выбранным индеском, сохраняем в
    правильном ответе. Заменяем в ряду число под выбранным индексом на '..'.
    Запрашивает ответ у пользователя. Функция возвращает пару ответ,
    верный_ответ
    """
    step = rr(-20, 20)
    len_row = rr(5, 11)
    start = rr(-50, 51)
    row = [start]
    for _ in range(len_row):
        row.append(row[-1] + step)
    secret_index = rr(1, len(row) - 1)
    true_answer = row[secret_index]                # В первом варианте решения
    row[secret_index] = '..'    # числа в ряду конвертировались в строки через
    print('Question: ', *row)   # list(map(str, row)), затем в принт собирались
    answer = prompt.string('Your answer: ')      # в строку через " ".join(row)
    if answer.isdigit() or answer[1:].isdigit() and answer[0] == '-':
        answer = int(answer)
    return answer, true_answer


def main():
    game_logic(game_rules, game_progression)


if __name__ == '__main__':
    main()
