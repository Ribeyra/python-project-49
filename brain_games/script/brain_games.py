#!/usr/bin/env python3
from brain_games.cli import welcome_user


def main():
    text = 'Welcome to the Brain Games!'
    print(text)
    name = welcome_user()
    print(f'Hello, {name}')


if __name__ == '__main__':
    main()
