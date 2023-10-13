from brain_games.cli import welcome_user


def verify_answer(game_foo) -> bool:
    answer, true_answer = game_foo()
    if answer == true_answer:
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{true_answer}'")
        return False


def game(game_foo) -> bool:
    rounds = 3
    for _ in range(rounds):
        if verify_answer(game_foo):
            print('Correct!')
        else:
            return False
    else:
        return True


def game_logic(game_rules, game_foo):
    text = 'Welcome to the Brain Games!'
    print(text)
    name = welcome_user()
    print(f'Hello, {name}')
    print(game_rules)
    if game(game_foo):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def main():
    pass


if __name__ == '__main__':
    main()
