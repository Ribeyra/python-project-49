import prompt


def welcome_user() -> str:
    name = prompt.string('May I have your name? ')
    return name


def main():
    pass


if __name__ == '__main__':
    main()
