#!/usr/bin/env python
import argparse

from character import Character


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--level", dest="level", action="store", type=int, default=1)
    parser.add_argument("name", action="store", default=["_"*20], nargs='*')
    args = parser.parse_args()
    char = Character(name=" ".join(args.name), level=args.level)
    print char
