#!/usr/bin/env python

import random
import argparse
from collections import OrderedDict


class Descriptors(object):

    physique = ["Athletic", "Brawny", "Corpulent", "Delicate", "Gaunt", "Hulking", "Lanky", "Ripped",
                "Rugged", "Scrawny", "Short", "Sinewy", "Slender", "Flabby", "Statuesque", "Stout",
                "Tiny", "Towering", "Willowy", "Wiry"]
    face = ["Bloated", "Blunt", "Bony", "Chiseled", "Delicate", "Elongated", "Patrician", "Pinched",
            "Hawkish", "Broken", "Impish", "Narrow", "Ratlike", "Round", "Sunken", "Sharp", "Soft",
            "Square", "Wide", "Wolfish"]
    skin = ["Battle Scar", "Birthmark", "Burn Scar", "Dark", "Makeup", "Oily", "Pale", "Perfect",
            "Pierced", "Pockmarked", "Reeking", "Tattooed", "Rosy", "Rough", "Sallow", "Sunburned",
            "Tanned", "War Paint", "Weathered", "Whip Scar"]
    hair = ["Bald", "Braided", "Bristly", "Cropped", "Curly", "Disheveled", "Dreadlocks", "Filthy",
            "Frizzy", "Greased", "Limp", "Long", "Luxurious", "Mohawk", "Oily", "Ponytail", "Silky",
            "Topknot", "Wavy", "Wispy"]
    clothing = ["Antique", "Bloody", "Ceremonial", "Decorated", "Eccentric", "Elegant", "Fashionable",
                "Filthy", "Flamboyant", "Stained", "Foreign", "Frayed", "Frumpy", "Livery", "Oversized",
                "Patched", "Perfumed", "Rancid", "Torn", "Undersized"]
    virtues = ["Ambitious", "Cautious", "Courageous", "Courteous", "Curious", "Disciplined", "Focused",
               "Generous", "Gregarious", "Honest", "Honorable", "Humble", "Idealistic", "Just", "Loyal",
               "Merciful", "Righteous", "Serene", "Stoic", "Tolerant"]
    vices = ["Aggressive", "Arrogant", "Bitter", "Cowardly", "Cruel", "Deceitful", "Flippant", "Gluttonous",
             "Greedy", "Irascible", "Lazy", "Nervous", "Prejudiced", "Reckless", "Rude", "Suspicious", "Vain",
             "Vengeful", "Wasteful", "Whiny"]
    speech = ["Blunt", "Booming", "Breathy", "Cryptic", "Drawling", "Droning", "Flowery", "Formal",
              "Gravelly", "Hoarse", "Mumbling", "Precise", "Quaint", "Rambling", "Rapid-fire", "Dialect",
              "Slow", "Squeaky", "Stuttering", "Whispery"]
    background = ["Alchemist", "Beggar", "Butcher", "Burglar", "Charlatan", "Cleric", "Cook", "Cultist",
                  "Gambler", "Herbalist", "Magician", "Mariner", "Mercenary", "Merchant", "Outlaw",
                  "Performer", "Pickpocket", "Smuggler", "Student", "Tracker"]
    misfortunes = ["Abandoned", "Addicted", "Blackmailed", "Condemned", "Cursed", "Defrauded", "Demoted",
                   "Discredited", "Disowned", "Exiled", "Framed", "Haunted", "Kidnapped", "Mutilated",
                   "Poor", "Pursued", "Rejected", "Replaced", "Robbed", "Suspected"]
    alignment = ["Law", "Law", "Law", "Law", "Law",
                 "Neutrality", "Neutrality", "Neutrality", "Neutrality", "Neutrality",
                 "Neutrality", "Neutrality", "Neutrality", "Neutrality", "Neutrality",
                 "Chaos", "Chaos", "Chaos", "Chaos", "Chaos"]

    @classmethod
    def format_description(cls, name):
        choices = {"name": name,
                   "physique": random.choice(cls.physique).lower(),
                   "face": random.choice(cls.face).lower(),
                   "skin": random.choice(cls.skin).lower(),
                   "hair": random.choice(cls.hair).lower(),
                   "clothing": random.choice(cls.clothing).lower(),
                   "virtue": random.choice(cls.virtues).lower(),
                   "vice": random.choice(cls.vices).lower(),
                   "speech": random.choice(cls.speech).lower(),
                   "background": random.choice(cls.background).lower(),
                   "misfortune": random.choice(cls.misfortunes).lower(),
                   "alignment": random.choice(cls.alignment).lower()}
        description_strings = ["  - Has a {physique} physique, a {face} face, {skin} skin and {hair} hair."
                               "\n  - Clothes are {clothing}, and speech {speech}."
                               "\n  - Is {virtue}, but {vice}."
                               "\n  - Has been a {background} in the past. Has been {misfortune} in the past."
                               "\n  - Favours {alignment}."]
        description = "".join(description_strings).format(**choices)
        return '\n'.join(['Description:', '-'*12, description])


class Tables(object):
    weapons = [("Dagger", 1), ("Cudgel", 1), ("Sickle", 1), ("Staff", 1),
               ("Spear", 2), ("Sword", 2), ("Axe", 2), ("Flail", 2), ("Mace", 2),
               ("Halberd (2h)", 3), ("War Hammer (2h)", 3), ("Long Sword (2h)", 3), ("Battle Axe (2h)", 3),
               ("Sling", 1), ("Bow", 2), ("Crossbow", 3)]

    # (Armor name, defense, slots)
    armor = [(range(1, 4), "No armor", 11, 0),
             (range(4, 15), "Gambeson", 12, 1),
             (range(15, 20), "Brigandine", 13, 2),
             (range(20, 21), "Chain", 14, 3)]

    # (Armor name, +defense, slots)
    helmet_shield = [(range(1, 14), []),
                     (range(14, 17), [("Helmet", 1, 1)]),
                     (range(17, 20), [("Shield", 1, 1)]),
                     (range(20, 21), [("Shield", 1, 1), ("Helmet", 1, 1)])]

    dungeon_gear = ["Rope, 50ft", "Pulleys", "Candles, 5", "Chain, 10ft", "Chalk, 10",
                    "Crowbar", "Tinderbox", "Grap. hook", "Hammer", "Waterskin",
                    "Lantern", "Lamp oil", "Padlock", "Manacles", "Mirror", "Pole, 10ft",
                    "Sack", "Tent", "Spikes, 5", "Torch, 5"]

    general_gear_1 = ["Air bladder", "Bear trap", "Shovel", "Bellows", "Grease", "Saw",
                      "Bucket", "Caltrops", "Chisel", "Drill", "Fish. rod", "Marbles",
                      "Glue", "Pick", "Hourglass", "Net", "Tongs", "Lockpicks",
                      "Metal file", "Nails"]

    general_gear_2 = ["Incense", "Sponge", "Lens", "Perfume", "Horn", "Bottle", "Soap",
                      "Spyglass", "Tar pot", "Twine", "Fake jewels", "Blank book",
                      "Card deck", "Dice set", "Cook pots", "Face paint", "Whistle",
                      "Instrument", "Quill & Ink", "Small bell"]


class NoSpaceError(Exception):
    pass


class Character(object):

    def __init__(self, name="_"*20, level=1):
        self.name = name
        self.level = level
        self.xp = 1000 * (level - 1)
        self.inventory = []
        self.armor_defense = 0

        self.stats = self.create_stats()
        self.hit_points = self._1d8()

        self.create_stats()
        self.basic_loadout()

        for x in range(level - 1):
            self._levelup(x+2)

    def __str__(self):
        return "\n\n\n".join([self.format_basic(),
                              self.format_stats(),
                              self.format_inventory(),
                              Descriptors.format_description(self.name)])

    def get_inventory(self):
        return self.inventory

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
            stat_strings.append(format_string.format(str(10+bonus), stat, str(bonus)))
        stat_strings.append("")
        stat_strings.append(format_string.format(str(self.armor_defense),
                            "Armor", str(self.armor_defense-10)))
        return "\n".join(stat_strings)

    def format_inventory(self):
        format_string = "{0: <25}{1: <10}{2:^15}"
        used_slots = 0
        inventory_strings = []
        inventory_strings.append("-"*50)
        for item in self.inventory:
            used_slots += item[2]
            inventory_strings.append(format_string.format(item[0], item[1], str(item[2])))
        inventory_strings.insert(0, format_string
                                 .format("Item", "Type", "Slots %s/%s" % (used_slots, self.slots)))
        return "\n".join(inventory_strings)

    def add_to_inventory(self, item, item_type, slots):
        if sum([x[2] for x in self.inventory]) > self.slots:
            raise NoSpaceError
        self.inventory.append([item, item_type, slots])

    def create_stats(self):
        stats = OrderedDict()
        stats["Strength"] = min(self._3d6())
        stats["Dexterity"] = min(self._3d6())
        stats["Constitution"] = min(self._3d6())
        stats["Intelligence"] = min(self._3d6())
        stats["Wisdom"] = min(self._3d6())
        stats["Charisma"] = min(self._3d6())

        return stats

    def basic_loadout(self):
        self.add_weapon()
        self.add_armor()
        self.add_gear()
        self.add_rations()

    def add_weapon(self):
        weapon, slots = random.choice(Tables.weapons)
        self.add_to_inventory(weapon, "Weapon", slots)
        if weapon in ("Bow", "Crossbow"):
            self.add_to_inventory("Arrors (20)", "Weapon", 1)

    def add_rations(self):
        self.add_to_inventory("Travel rations (1 day)", "Food", 1)
        self.add_to_inventory("Travel rations (1 day)", "Food", 1)

    def add_armor(self):
        choice = random.randint(1, 20)
        for armor in Tables.armor:
            if choice in armor[0]:
                _, name, armor_defense, slots = armor
                self.add_to_inventory(name, "Armor", slots)
                self.armor_defense = armor_defense
                break

        choice = random.randint(1, 20)
        for helmet_shield in Tables.helmet_shield:
            if choice in helmet_shield[0]:
                for item in helmet_shield[1]:
                    name, armor_defense, slots = item
                    self.add_to_inventory(name, "Armor", slots)
                    self.armor_defense += armor_defense
                break

    def add_gear(self):
        self.add_to_inventory(random.choice(Tables.dungeon_gear), "Gear", 1)
        self.add_to_inventory(random.choice(Tables.dungeon_gear), "Gear", 1)
        self.add_to_inventory(random.choice(Tables.general_gear_1), "Gear", 1)
        self.add_to_inventory(random.choice(Tables.general_gear_2), "Gear", 1)

    @property
    def slots(self):
        return self.stats["Constitution"] + 10

    def _3d6(self):
        return [random.randint(1, 6),
                random.randint(1, 6),
                random.randint(1, 6)]

    def _1d8(self):
        return random.randint(1, 8)

    def _1d20(self):
        return random.randint(1, 20)

    def _levelup(self, iteration):
        count = 3
        stats = self.stats.keys()
        while count > 0:
            for stat in random.sample(stats, len(stats)):
                if (self.stats[stat] < 10) and (self._1d20() < (10 + self.stats[stat])):
                    self.stats[stat] += 1
                    count -= 1
                    break
        hp = sum([self._1d8() for x in range(iteration)])
        if hp < self.hit_points:
            self.hit_points += 1
        else:
            self.hit_points = hp


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--name", dest="name", action="store", default="_"*20)
    parser.add_argument("--level", dest="level", action="store", type=int, default=1)
    args = parser.parse_args()
    char = Character(name=args.name, level=args.level)
    print char
