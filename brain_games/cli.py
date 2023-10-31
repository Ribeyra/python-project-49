import prompt
from brain_games.constants import GREETINGS


def welcome_user() -> str:
    """
    Выводит в терминал приглашение. Запрашивает имя пользователя
    и приветствует его по имени. Возвращает имя пользователя.
    """
    print(GREETINGS)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name
