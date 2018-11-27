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
        self.level = level
        self.xp = 1000 * (level - 1)
        self.inventory = Inventory(self)

        self.stats = self.create_stats()
        self.hit_points = dice.roll('1d8')[0]

        self.create_stats()
        self.basic_loadout()
        self.traits = Traits()

        for x in range(level - 1):
            self._levelup(x+2)

    def __str__(self):
        return "\n\n\n".join([self.format_basic(),
                              self.format_stats(),
                              str(self.inventory),
                              str(self.traits)])

    def __repr__(self):
        character = OrderedDict([('id', self.id),
                                 ('name', self.name),
                                 ('xp', self.xp),
                                 ('level', self.level),
                                 ('hit_points', self.hit_points),
                                 ('attributes', self.stats),
                                 ('armor_defense', self.inventory.armor_defense),
                                 ('inventory', [item.details for item in self.inventory.sorted()]),
                                 ('used_slots', self.inventory.used_slots),
                                 ('total_slots', self.inventory.total_slots),
                                 ('traits', self.traits.traits)]
                                )

        return json.dumps(character)

    @property
    def armor_defense(self):
        return self.inventory.armor_defense

    def format_basic(self):
        basic_strings = []
        basic_strings.append("Name: {0: ^20}".format(self.name))
        basic_strings.append("XP: {0: >6}   Level: {1: <2}"
                             .format(str(self.xp), str(self.level)))
        return " ".join(basic_strings)

    def format_stats(self):
        format_string = "{0: ^15}{1: ^20}{2: ^15}"
        stat_strings = []

        stat_strings.append("Hit Points: %s / %s" % (self.hit_points, self.hit_points))
        stat_strings.append("")

        stat_strings.append(format_string.format("Defense", "Ability", "Bonus"))
        stat_strings.append("-"*50)
        for stat, bonus in self.stats.iteritems():
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

    def basic_loadout(self):
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
        self.inventory.add(Items.get('general_gear_1'))

    def _levelup(self, iteration):
        count = 3
        stats = self.stats.keys()
        while count > 0:
            for stat in random.sample(stats, len(stats)):
                if (self.stats[stat] < 20) and (dice.roll('1d20')[0] < (self.stats[stat])):
                    self.stats[stat] += 1
                    count -= 1
                    break
        hp = sum([dice.roll('1d8')[0] for x in range(iteration)])
        if hp < self.hit_points:
            self.hit_points += 1
        else:
            self.hit_points = hp
