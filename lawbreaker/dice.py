import re
import random

from exceptions import InvalidDiceFormat


class Dice(object):
    def __getattr__(self, key):
        try:
            count, sides = re.match('_([0-9]+)d([0-9]+)', key).groups()
        except AttributeError:
            raise InvalidDiceFormat(key)

        def dice():
            return [random.randint(1, int(sides)) for x in range(int(count))]

        return dice

    def _1d1(self):
        assert self.__getattr__('_1d1') == [1]
        return self.__getattr__('_1d1')


dice = Dice()
