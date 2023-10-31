import prompt
import random
from brain_games.engine import game_engine
from brain_games.constants import GAME_RULES_GCD, LIMITS, NUMS_AMOUNT


def _get_gcd(nums: list[int]) -> int:
    """
    В качестве аргумента принимает список с 2 числами.
    Возвращает наибольший общий делитель для чисел из списка.
    """
    if nums[1] == 0:                        # Вариант бинарного алгоритма,
        return nums[0]                      # предложенный ChatGPT
    return _get_gcd([nums[1], nums[0] % nums[1]])


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


def _game_gcd() -> tuple:
    """
    Функция game_gcd определяет логику игры по определению наибольшего
    общего делителя. Сначала создается список из 2 случайных чисел. Далее
    для указанных чисел, с помощью рекурсивной функции get_gcd находится НОД.
    Затем у пользователя запрашивается его вариант ответа. Функция возвращает
    пару ответ, верный_ответ
    """
    nums = [random.randrange(LIMITS[0], LIMITS[1]) for _ in range(NUMS_AMOUNT)]
    print(f'Question: {nums[0]} {nums[1]}')
    correct_answer = str(_get_gcd(nums))
    answer = prompt.string('Your answer: ')
    return answer, correct_answer


def run_game_gcd():
    """
    Запускает игру
    """
    game_engine(GAME_RULES_GCD, _game_gcd)
