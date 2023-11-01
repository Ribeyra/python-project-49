import prompt
from brain_games.cli import welcome_user
from brain_games.constants import ROUNDS


def _run_loop_and_verify_answer(game_foo: callable) -> bool:
    """
    Единственным аргументом принимает функцию с логикой игры (game_foo).
    Функция содержит цикл, соответствующий кол-ву раундов (ROUNDS).
    game_foo возвращает значение за вопроса () и верный ответ. Затем
    запрашивается ответ пользователя. В цикле сравнивается ответ
    пользователя и верный ответ. Если ответы не совпадут, цикл прерывается
    и эта функция возвращает False. Иначе, если цикл завершается штатно,
    эта функция возвращает True.
    """
    for _ in range(ROUNDS):
        quest, correct_answer = game_foo()
        print('Question:', end=' ')
        if isinstance(quest, list) or isinstance(quest, tuple):
            print(*quest)
        else:
            print(quest)
        user_answer = prompt.string('Your answer: ').lower()
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            return False
    return True


def game_engine(game_rules: str, game_foo: callable) -> None:
    """
    game_engine - функция, запускающая выполнение игровой логики, общей для
    разных игр. В аргументы функции передается строка (game_rules) с
    правилами игры и функция (game_foo) содержащая логику конкретной игры.
    Далее game_foo передается в аргумент функции _run_loop_and_verify_answer.
    В зависимости от булевого значения, возвращаемого функцией
    _run_loop_and_verify_answer происходит выбор завершающего сообщения
    """
    name = welcome_user()
    print(game_rules)
    if _run_loop_and_verify_answer(game_foo):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
