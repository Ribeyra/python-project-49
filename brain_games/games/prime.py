import prompt
import random
from brain_games.engine import game_engine
from brain_games.constants import GAME_RULES_PRIME, LIMIT


def _is_prime(num: int) -> bool:
    """
    В качестве аргумента принимает число int.
    Функция ищет делитель в диапазоне от 2 до корня из числа, при делении на
    который не будет остатка. Если такой делитель найден, число не является
    простым.
    """
    for divisor in range(2, int(num ** (0.5)) + 1):
        if num % divisor == 0:
            return False
    return True


def _game_prime() -> tuple:
    """
    Функция game_prime определяет логику игры «Простое ли число?». На первом
    шаге получаем случайное число. С помощью функции is_prime определяем
    является ли полученное число простым и верный ответ. Затем запрашиваем
    ответ пользователя. Функция возвращает пару ответ, верный_ответ
    В процессе тестирования обнаружил, что скрипт не так часто генерирует
    простые числа. Статистически это оправданно, простых чисел меньше чем
    составных. Можно изменить скрипт, так, что бы он сначала определял какое
    будет предлагать пользователю простое или составное, а затем генерировал
    соответсвующее... Если потребуется, сделаю это позже.
    """
    num = random.randrange(LIMIT)
    correct_answer = 'yes' if _is_prime(num) else 'no'
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ').lower()
    return answer, correct_answer


def run_game_prime():
    """
    Запускает игру
    """
    game_engine(GAME_RULES_PRIME, _game_prime)
