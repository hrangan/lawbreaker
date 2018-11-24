#!/usr/bin/env python
import argparse

from character import Character
from names import Name

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--level", dest="level", action="store", type=int, default=1)
    parser.add_argument('--random-name', action='store_const', dest='randomName', const=True)
    parser.add_argument("name", action="store", default=["_"*20], nargs='*')
    args = parser.parse_args()
    char = Character(name=args.randomName and Name.get() or " ".join(args.name), level=args.level)
    print char
