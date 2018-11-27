import re
import random

from exceptions import InvalidDiceFormat


class Dice(object):
    def roll(self, key):
        try:
            count, sides = re.match('^([0-9]+)d([0-9]+)', key).groups()
        except AttributeError:
            raise InvalidDiceFormat(key)

        return [random.randint(1, int(sides)) for x in range(int(count))]


dice = Dice()
