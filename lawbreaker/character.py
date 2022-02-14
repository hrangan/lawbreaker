import json
import uuid
import random

from collections import OrderedDict

from lawbreaker.dice import dice
from lawbreaker.inventory import Inventory
from lawbreaker.exceptions import InventoryFullException
from lawbreaker.items import Items, Food, Gear
from lawbreaker.traits import Traits


class Character(object):

    def __init__(self, name="_"*20, level=1):
        self.id = uuid.uuid4().hex
        self.name = name

        self.stats = self.create_stats()
        self.hit_points = dice.roll('1d8')[0]
        self.traits = Traits()

        self.inventory = Inventory(self)
        self._basic_loadout()

        self.level = 1
        self.xp = 0
        self.progression_history = {self.level: {'hit_points': self.hit_points,
                                                 'xp': 0,
                                                 'attributes': OrderedDict(self.stats)}
                                    }
        for x in range(level - 1):
            self.levelup()

    def __str__(self):
        return "\n\n\n".join([self._format_basic(),
                              self._format_stats(),
                              str(self.inventory),
                              str(self.traits)])

    def __repr__(self):
        # TODO data sent to the server is at level 10. need to work out a way
        # of keeping the character at level 1, but still doing progression
        # correctly
        character = {
                     # Static
                     'id': self.id,
                     'name': self.name,
                     'armor_defense': self.inventory.armor_defense,
                     'inventory': [item.details for item in self.inventory.sorted()],
                     'traits': self.traits.traits,
                     'used_slots': self.inventory.used_slots,

                     # Level up tracking
                     'progression': self.progression_history}

        return json.dumps(character)

    @property
    def armor_defense(self):
        return self.inventory.armor_defense

    def _format_basic(self):
        basic_strings = []
        basic_strings.append("Name: {0: ^20}".format(self.name))
        basic_strings.append("XP: {0: >6}   Level: {1: <2}"
                             .format(str(self.xp), str(self.level)))
        return " ".join(basic_strings)

    def _format_stats(self):
        format_string = "{0: ^15}{1: ^20}{2: ^15}"
        stat_strings = []

        stat_strings.append("Hit Points: %s / %s" % (self.hit_points, self.hit_points))
        stat_strings.append("")

        stat_strings.append(format_string.format("Defense", "Ability", "Bonus"))
        stat_strings.append("-"*50)
        for stat, bonus in self.stats.items():
            stat_strings.append(format_string.format(str(bonus), stat.title(), str(bonus - 10)))
        stat_strings.append("")
        stat_strings.append(format_string.format(str(self.armor_defense),
                            "Armor", str(self.armor_defense - 10)))
        return "\n".join(stat_strings)

    def create_stats(self):
        stats = OrderedDict([("strength", 10 + min(dice.roll('3d6'))),
                             ("dexterity", 10 + min(dice.roll('3d6'))),
                             ("constitution", 10 + min(dice.roll('3d6'))),
                             ("intelligence", 10 + min(dice.roll('3d6'))),
                             ("wisdom", 10 + min(dice.roll('3d6'))),
                             ("charisma", 10 + min(dice.roll('3d6')))]
                            )

        return stats

    def _basic_loadout(self):
        while True:
            try:
                self.add_gear()
                self.add_rations()
                self.add_armor()
                self.add_weapon()
            except InventoryFullException:
                self.inventory.delete_all()
                continue
            else:
                break

    def add_weapon(self):
        weapon = Items.get('weapon')
        self.inventory.add(weapon, equip=True)
        if weapon.name in ("Bow", "Crossbow"):
            self.inventory.add(Gear("Arrows, 20"))

    def add_rations(self):
        self.inventory.add(Food("Travel rations (1 day)"))
        self.inventory.add(Food("Travel rations (1 day)"))

    def add_armor(self):
        self.inventory.add(Items.get('armor'), equip=True)
        self.inventory.add(Items.get('helmet_shield'), equip=True)

    def add_gear(self):
        self.inventory.add(Items.get('dungeon_gear'))
        self.inventory.add(Items.get('dungeon_gear'))
        self.inventory.add(Items.get('general_gear_1'))
        self.inventory.add(Items.get('general_gear_2'))

    def levelup(self):
        count = 3
        self.level += 1
        attributes = list(self.stats)
        while count > 0:
            random.shuffle(attributes)
            for attribute in attributes:
                if (self.stats[attribute] < 20) and (dice.roll('1d20')[0] < (self.stats[attribute])):
                    self.stats[attribute] += 1
                    count -= 1
                    if count == 0:
                        break
        hp = sum([dice.roll('1d8')[0] for x in range(self.level)])
        if hp < self.hit_points:
            hp = self.hit_points + 1
        else:
            self.hit_points = hp

        self.progression_history[self.level] = {'hit_points': hp,
                                                'xp': 1000 * (self.level - 1),
                                                'attributes': OrderedDict(self.stats)}
