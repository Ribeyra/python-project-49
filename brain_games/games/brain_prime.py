#!/usr/bin/env python3
import prompt
from random import randrange as rr
from brain_games.logic import game_logic

game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int) -> bool:
    """
    Для проверки на простоту использовал часть функции, которая собирала
    список делителей. Функцию собиравшую список делителей сам написал в
    марте, выполняя задание на stepik.org
    Функция ищет делитель в диапазоне от 2 до корня из числа, при делении на
    который не будет остатка. Если такой делитель найден, число не является
    простым.
    """
    for divisor in range(2, int(num ** (0.5)) + 1):
        if num % divisor == 0:
            return False
    else:
        return True
#   Оказалось, что время выполнения моей функции и функции с сайта foxford.ru
#   отличается на уровне статистической погрешности.
#    """
#    Алгоритм проверки на простоту взял с сайта
#    https://foxford.ru/wiki/informatika/proverka-chisla-na-prostotu-v-python
#    """
#    if num % 2 == 0:
#        return num == 2
#    d = 3
#    while d * d <= num and num % d != 0:
#        d += 2
#    return d * d > num


def game_prime() -> tuple:
    """
    Функция game_prime определяет логику игры «Простое ли число?». На первом
    шаге получаем случайное число. С помощью функции is_prime определяем
    является ли полученное число простым, из чего получем верный ответ. Затем
    запрашиваем ответ пользователя. Функция возвращает пару ответ, верный_ответ
    В процессе тестирования обнаружил, что скрипт не так часто генерирует
    простые числа. Статистически это оправданно, простых чисел меньше чем
    составных. Можно изменить скрипт, так, что бы он сначала определял какое
    будет предлагать пользователю простое или составное, а затем генерировал
    соответсвующее... Если потребуется, сделаю это позже.
    """
    num = rr(201)
    true_answer = 'yes' if is_prime(num) else 'no'
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ').lower()
    return answer, true_answer


def main():
    game_logic(game_rules, game_prime)


if __name__ == '__main__':
    main()
