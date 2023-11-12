import prompt
from brain_games.cli import welcome_user
from brain_games.constants import ROUNDS


def _get_user_answer(quest: str) -> str:
    print('Question:', end=' ')
    if isinstance(quest, (list, tuple)):
        print(*quest)
    else:
        print(quest)
    user_answer = prompt.string('Your answer: ').lower()
    return user_answer


def _verify_answer(game_foo: callable) -> bool:
    quest, correct_answer = game_foo()
    user_answer = _get_user_answer(quest)
    if user_answer == correct_answer:
        print('Correct!')
        return True
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'")
    return False


def _run_loop(game_foo: callable) -> bool:
    for _ in range(ROUNDS):
        if not _verify_answer(game_foo):
            return False
    return True


def game_engine(game_rules: str, game_foo: callable) -> None:
    name = welcome_user()
    print(game_rules)
    if _run_loop(game_foo):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
