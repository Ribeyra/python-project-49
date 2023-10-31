from brain_games.cli import welcome_user
from brain_games.constants import ROUNDS


def _run_loop_and_verify_answer(game_foo: callable) -> bool:
    """
    Единственным аргументом принимает функцию с логикой игры.
    Функция содержит цикл, соответствующий кол-ву раундов (ROUNDS).
    В цикле сравнивается верный ответ и ответ пользователя, возвращаемые
    функцией, содержащей логику игры (game_foo). Если ответы не совпадут,
    цикл прерывается и эта функция возвращает False. Иначе, если цикл
    завершается штатно, эта функция возвращает True
    """
    for _ in range(ROUNDS):
        answer, correct_answer = game_foo()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
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
