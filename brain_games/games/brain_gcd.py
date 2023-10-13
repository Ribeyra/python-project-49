#!/usr/bin/env python3
import prompt
from random import randrange as rr
from brain_games.logic import game_logic

game_rules = 'Find the greatest common divisor of given numbers.'


def gcd(nums: list[int]):   # noqa: C901
    nums.sort()
    if nums[0] == 0 or nums[0] == nums[1]:
        return nums[1]
    elif nums[0] == 1:
        return 1
    elif nums[0] % 2 == 0 and nums[1] % 2 == 0:
        return 2 * gcd([nums[0] // 2, nums[1] // 2])
    elif nums[0] % 2 == 0 and nums[1] % 2 == 1:
        return gcd([nums[0] // 2, nums[1]])
    elif nums[0] % 2 == 1 and nums[1] % 2 == 0:
        return gcd([nums[0], nums[1] // 2])
    elif nums[0] % 2 == 1 and nums[1] % 2 == 1:
        return gcd([nums[0], (nums[1] - nums[0]) // 2])


def game_gcd() -> tuple:
    nums = [rr(1, 101) for _ in range(2)]
    print(f'Question: {nums[0]} {nums[1]}')
    true_answer = gcd(nums)
    answer = prompt.string('Your answer: ')
    if answer.isdigit():
        answer = int(answer)
    return answer, true_answer


def main():
    game_logic(game_rules, game_gcd)


if __name__ == '__main__':
    main()
