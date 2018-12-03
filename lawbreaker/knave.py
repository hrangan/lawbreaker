#!/usr/bin/env python
import argparse

from lawbreaker.character import Character
from lawbreaker.names import Name


def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--level", dest="level", action="store", type=int, default=1,
                        choices=range(1, 11))

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--random-name', action='store_const', dest='randomName', const=True)
    group.add_argument("name", action="store", default=["_"*20], nargs='*')

    args = parser.parse_args()
    char = Character(name=args.randomName and Name.get() or " ".join(args.name), level=args.level)
    print(char)


if __name__ == "__main__":
    main()
