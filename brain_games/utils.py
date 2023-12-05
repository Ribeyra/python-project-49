import random


def get_random_num(list_value: list[int]) -> int:
    """
    Generate a random number based on the provided list.

    param list_value: A list that includes one or two values.
        - If one value is in the list, it is interpreted as the stop value.
        The start value takes the default value of 0.
        - If two values are in the list, the first is interpreted as the start
        value, and the last as the stop value.

    return: A random integer from start to stop (inclusive).

    Note:
        If the list has an invalid number of elements, a string describing the
        issue is returned.
        (This is due to project constraints;
        no *args, raise, or except is allowed.)
    """
    if len(list_value) == 1:
        return random.randrange(list_value[0] + 1)
    elif len(list_value) == 2:
        return random.randrange(list_value[0], list_value[1] + 1)
    else:
        return (
            'эта строка ложит программу, т.к. функция получила список с '
            'неверным кол-вом элементов'
        )
