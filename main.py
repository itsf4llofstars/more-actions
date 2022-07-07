#!/usr/bin/env python3
import random


def pick_number() -> int:
    return random.randint(1, 100)


def main():
    cops_num = pick_number()


if __name__ == '__main__':
    import sys

    sys.exit(main())