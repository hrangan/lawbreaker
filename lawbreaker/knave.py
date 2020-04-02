#!/usr/bin/env python
import argparse

from lawbreaker.character import Character
from lawbreaker.names import Name


class CustomFormatter(argparse.HelpFormatter):
    def _format_args(self, action, default_metavar):
        if action.nargs == argparse.ZERO_OR_MORE:
            get_metavar = self._metavar_formatter(action, default_metavar)
            result = '[%s]' % get_metavar(1)
            return result
        else:
            return super()._format_args(action, default_metavar)

    def _metavar_formatter(self, action, default_metavar):
        if action.choices is not None:
            result = '{%s - %s}' % (action.choices[0], action.choices[-1])
            return lambda tuple_size: (result, ) * tuple_size
        else:
            return super()._metavar_formatter(action, default_metavar)


def main():
    parser = argparse.ArgumentParser(description="Create a random character for the Knave roleplaying game",
                                     formatter_class=CustomFormatter)
    parser.add_argument("--level", dest="level", action="store", type=int, default=1,
                        choices=range(1, 11), help='select a character level (optional)')

    parser.add_argument('name', action='store', default=[], nargs='*',
                        help='name your character (optional)')

    args = parser.parse_args()
    char = Character(name=' '.join(args.name) or Name.get(), level=args.level)
    print(char)


if __name__ == "__main__":
    main()
