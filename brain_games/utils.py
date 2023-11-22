import random


def get_random_num(*args) -> int:
    if len(args) == 2:
        return random.randint(*args)
    return random.randrange(*args)
