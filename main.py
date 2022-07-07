#!/usr/bin/env python3
import random


def pick_number() -> int:
    return random.randint(1, 100)


def player_number() -> int:
    return int(input("Enter your guess: "))


def check_number(computer, player):
    if player < computer:
        return "LOW"
    elif player > computer:
        return "HIGH"
    return "WIN"


def main():
    comps_num = pick_number()
    users_num = player_number()
    num_status = check_number(comps_num, users_num)
    print(f"Your Guess: {num_status}")


if __name__ == "__main__":
    import sys

    sys.exit(main())
