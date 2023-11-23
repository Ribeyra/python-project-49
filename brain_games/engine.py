import prompt
from brain_games.constants import ROUNDS, GREETINGS


def greet(rule: str) -> str:
    print(GREETINGS)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(rule)
    return name


def printing_message(*args, end_game=False) -> None:
    is_win, *args = args
    if not end_game:
        if is_win:
            print('Correct!')
        else:
            print(f"'{args[1]}' is wrong answer ;(. "
                  f"Correct answer was '{args[0]}'")
    else:
        if is_win:
            print(f'Congratulations, {args[0]}!')
        else:
            print(f"Let's try again, {args[0]}!")


def get_user_answer(quest: str) -> str:
    if isinstance(quest, list):
        quest = ' '.join([str(el) for el in quest])
    print(f'Question: {quest}')
    user_answer = prompt.string('Your answer: ').lower()
    return user_answer


def user_answer_is_correct(game_foo: callable) -> bool:
    quest, correct_answer = game_foo()
    user_answer = get_user_answer(quest)
    is_correct = user_answer == correct_answer
    printing_message(is_correct, correct_answer, user_answer)
    return is_correct


def play_game(game_rule: str, game_foo: callable) -> None:
    name = greet(game_rule)
    is_win = True
    for _ in range(ROUNDS):
        if not user_answer_is_correct(game_foo):
            is_win = False
            break
    printing_message(is_win, name, end_game=True)
