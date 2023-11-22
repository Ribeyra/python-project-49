import prompt
from brain_games.constants import ROUNDS, GREETINGS


def printing_message(*args, greetings=False, end_game=False, name=[]) -> None:
    is_win = args[0] if not greetings else None
    if greetings:
        print(GREETINGS)
        name.append(prompt.string('May I have your name? '))
        print(f'Hello, {name[0]}')
        print(args[0])
    elif not end_game:
        if is_win:
            print('Correct!')
        else:
            print(f"'{args[2]}' is wrong answer ;(. "
                  f"Correct answer was '{args[1]}'")
    else:
        if is_win:
            print(f'Congratulations, {name[0]}!')
        else:
            print(f"Let's try again, {name[0]}!")


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


def run_loop(game_foo: callable) -> bool:
    for _ in range(ROUNDS):
        if not user_answer_is_correct(game_foo):
            return False
    return True


def play_game(game_rule: str, game_foo: callable) -> None:
    printing_message(game_rule, greetings=True)
    is_win = run_loop(game_foo)
    printing_message(is_win, end_game=True)
