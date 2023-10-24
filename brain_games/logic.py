from brain_games.cli import welcome_user
from brain_games.constants import ROUNDS, GREETINGS


def _verify_answer(game_foo: callable) -> bool:
    """
    Функция _verify_answer сравнивает верный ответ и ответ пользователя,
    возвращаемые функцие, в которой содержится логика игры (game_foo).
    В зависимости от результата сравнения, в функцию _game возвращается
    True или False
    """
    answer, true_answer = game_foo()
    if answer == true_answer:
        return True
    print(f"'{answer}' is wrong answer ;(. "
          f"Correct answer was '{true_answer}'")
    return False


def _run_loop(game_foo: callable) -> bool:
    """
    Функция _run_loop содержит цикл, соответсвующий кол-ву раундов
    (по умолчанию 3). В цикле происходит обращение к функции _verify_answer,
    которая проверяет правильность ответа. Если _verify_answer возвращает
    False, цикл прерывается и функция _run_loop возвращает False. Иначе, если
    цикл завершается штатно функция _run_loop возвращает True
    """
    for _ in range(ROUNDS):
        if _verify_answer(game_foo):
            print('Correct!')
        else:
            return False
    return True


def game_logic(game_rules: str, game_foo: callable) -> None:
    """
    game_logic - функция, запускающая выполнение игровой логики, общей для
    разных игр. В аргументы функции передается строка (game_rules) с
    правилами игры и функция (game_foo) содержащая логику конкретной игры.
    Далее game_foo передается в аргумент функции _game. В зависимости от
    булевого значения, возвращаемого функцией _game происходит выбор
    завершающего сообщения
    """
    print(GREETINGS)
    name = welcome_user()
    print(f'Hello, {name}')
    print(game_rules)
    if _run_loop(game_foo):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
