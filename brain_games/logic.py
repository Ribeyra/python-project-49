import prompt
from random import randrange as rr, choice
from brain_games.cli import welcome_user


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
    answer = int(prompt.string('Your answer: '))
    return answer, true_answer


def game_even() -> tuple:
    num = rr(101)    # generate random number in limit 101
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ').lower()
    true_answer = 'no' if num % 2 else 'yes'   # alt ('yes', 'no')[num % 2]
    return answer, true_answer


def verify_answer(type_game) -> bool:
    list_foo = {'even': game_even,
                'calc': game_calc,
                'tree': 1}
    current_foo = list_foo[type_game]
    answer, true_answer = current_foo()
    if answer == true_answer:
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{true_answer}'")
        return False


def game(type_game) -> bool:
    for _ in range(3):
        if verify_answer(type_game):
            print('Correct!')
        else:
            return False
    else:
        return True


def game_logic(type_game):
    text = 'Welcome to the Brain Games!'
    print(text)
    name = welcome_user()
    print(f'Hello, {name}')
    match type_game:
        case 'even':
            print('Answer "yes" if the number is even, otherwise answer "no".')
        case 'calc':
            print('What is the result of the expression?')
    if game(type_game):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def main():
    pass


if __name__ == '__main__':
    main()
