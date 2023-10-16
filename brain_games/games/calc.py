import prompt
from random import choice, randrange as rr


def game_calc() -> tuple:
    """
    Функция game_calc определяет логику игры "калькулятор". Первым шагом
    происходит случайный выбор математической операции. Затем случайным
    образом определяются опернады. В случае, если выбрано умножение, второй
    операнд ограничается 10 (мне кажется решать примеры типа 48 * 37 не лучшее
    развалечение). В зависимости от операнда, определяется верный ответ. Ответ
    пользователя проходит двойную проверку, это либо число, либо число с
    минусом в начале, т.к. правильный ответ может быть отрицательным. Возможно,
    проще было бы привести верный ответ к строке, но мне кажется, число должно
    быть числом. Функция возвращает пару ответ, верный_ответ
    """
    oper = choice(("+", "-", "*"))
    LIMIT = 51
    LIMIT_AT_MULT = 11
    num1, num2 = rr(LIMIT), rr(LIMIT_AT_MULT) if oper == '*' else rr(LIMIT)
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
    pass


if __name__ == '__main__':
    main()
