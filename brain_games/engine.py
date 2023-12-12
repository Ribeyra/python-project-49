import prompt
from brain_games.constants import ROUNDS, GREETINGS


def print_greet() -> None:
    print(GREETINGS)


def meet_user() -> str:
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def print_rule(rule: str) -> None:
    print(rule)


def print_round_message(is_correct: bool, answer: str, user_answer: str):
    if is_correct:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{answer}'")


def print_end_message(is_win: bool, name: str) -> None:
    if is_win:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def get_user_answer(quest: str) -> str:
    print(f'Question: {quest}')
    user_answer = prompt.string('Your answer: ').lower()
    return user_answer


def is_correct_user_answers(game_foo: callable) -> bool:
    for _ in range(ROUNDS):
        quest, correct_answer = game_foo()
        user_answer = get_user_answer(quest)
        is_correct = user_answer == correct_answer
        print_round_message(is_correct, correct_answer, user_answer)
        if not is_correct:
            return False
    return True


def play_game(game_rule: str, game_foo: callable) -> None:
    print_greet()
    name = meet_user()
    print_rule(game_rule)
    game_result = is_correct_user_answers(game_foo)
    print_end_message(game_result, name)
