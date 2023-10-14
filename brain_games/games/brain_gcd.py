#!/usr/bin/env python3
import prompt
from random import randrange as rr
from brain_games.logic import game_logic

game_rules = 'Find the greatest common divisor of given numbers.'


def gcd(nums: list[int]) -> int:
    if nums[1] == 0:                        # Вариант бинарного алгоритма,
        return nums[0]                      # предложенный ChatGPT
    return gcd([nums[1], nums[0] % nums[1]])


#    nums.sort()                             # Мой вариант решения с
#    if nums[0] == 0 or nums[0] == nums[1]:  # использованием бинарного
#        return nums[1]                      # алгоритма Евклида,
#    elif nums[0] == 1:                      # который я нашел на вики
#        return 1                            # https://w.wiki/7mfY
#    elif nums[0] % 2 == 0 and nums[1] % 2 == 0:
#        return 2 * gcd([nums[0] // 2, nums[1] // 2])
#    elif nums[0] % 2 == 0 and nums[1] % 2 == 1:
#        return gcd([nums[0] // 2, nums[1]])
#    elif nums[0] % 2 == 1 and nums[1] % 2 == 0:
#        return gcd([nums[0], nums[1] // 2])
#    elif nums[0] % 2 == 1 and nums[1] % 2 == 1:
#        return gcd([nums[0], (nums[1] - nums[0]) // 2])


def game_gcd() -> tuple:
    """
    Функция game_gcd определяет логику игры по определению наибольшего
    общего делителя. Сначала создается список из 2 случайных чисел. Далее
    для указанных чисел, с помощью рекурсивной функции gcd находится НОД.
    Затем у пользователя запрашивается его вариант ответа. Функция возвращает
    пару ответ, верный_ответ
    """
    nums = [rr(1, 101) for _ in range(2)]
    print(f'Question: {nums[0]} {nums[1]}')
    true_answer = gcd(nums)
    answer = prompt.string('Your answer: ')
    if answer.isdigit():
        answer = int(answer)
    return answer, true_answer


def main():
    game_logic(game_rules, game_gcd)


if __name__ == '__main__':
    main()
