#!/usr/bin/env python3
from brain_games.cli import welcome_user


def main():
    GREETINGS = 'Welcome to the Brain Games!'
    print(GREETINGS)
    name = welcome_user()
    print(f'Hello, {name}')


if __name__ == '__main__':
    main()
