import prompt
from brain_games.constants import ROUNDS, GREETINGS


def printing_greet(rule: str) -> str:
    print(GREETINGS)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(rule)
    return name


def printing_end_message(is_win, name) -> None:
    if is_win:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def printing_round_message(is_correct, correct_answer, user_answer) -> None:
    if is_correct:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'")


def get_user_answer(quest: str) -> str:
    print(f'Question: {quest}')
    user_answer = prompt.string('Your answer: ').lower()
    return user_answer


def user_answer_is_correct(game_foo: callable) -> bool:
    quest, correct_answer = game_foo()
    user_answer = get_user_answer(quest)
    is_correct = user_answer == correct_answer
    printing_round_message(is_correct, correct_answer, user_answer)
    return is_correct


def play_game(game_rule: str, game_foo: callable) -> None:
    name = printing_greet(game_rule)
    is_win = True
    for _ in range(ROUNDS):
        if not user_answer_is_correct(game_foo):
            is_win = False
            break
    printing_end_message(is_win, name)
