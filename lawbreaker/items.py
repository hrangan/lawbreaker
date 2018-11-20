import random
from collections import OrderedDict


class InvalidItemCategoryException(Exception):
    pass


class InvalidItemAttribute(Exception):
    pass


class BaseItem(object):
    type = None

    def __init__(self, item_name, slots=1):
        self.details = OrderedDict({'name':  item_name,
                                    'type':  self.__class__.type,
                                    'slots':  slots,
                                    'equipped': False})

    def equip(self):
        self.details['equipped'] = True
        return True

    def unequip(self):
        self.details['equipped'] = False
        return False

    def __getattr__(self, key):
        try:
            return self.details[key]
        except KeyError:
            return InvalidItemAttribute


class Weapon(BaseItem):
    type = 'Weapon'

    def __init__(self, item_name, slots, damage, hands, quality):
        super(Weapon, self).__init__(item_name, slots)
        self.details.update({'damage': damage,
                             'hands': hands,
                             'quality': quality})


class Armor(BaseItem):
    type = 'Armor'

    def __init__(self, item_name, slots, defense, quality):
        super(Armor, self).__init__(item_name, slots)
        self.details.update({'defense': defense,
                             'quality': quality})


class Gear(BaseItem):
    type = 'Gear'


class Food(BaseItem):
    type = 'Food'


class Items(object):
    @classmethod
    def get(self, item_type):
        try:
            items = getattr(self, item_type)
        except AttributeError:
            raise InvalidItemCategoryException
        return random.choice(items)

    weapon = [Weapon(item_name, slots, damage, hands, quality)
              for (item_name, slots, damage, hands, quality) in
              [("Dagger", 1, 'd6', 1, 3),
               ("Cudgel", 1, 'd6', 1, 3),
               ("Sickle", 1, 'd6', 1, 3),
               ("Staff", 1, 'd6', 1, 3),
               ("Spear", 2, 'd8', 1, 3),
               ("Sword", 2, 'd8', 1, 3),
               ("Axe", 2, 'd8', 1, 3),
               ("Flail", 2, 'd8', 1, 3),
               ("Mace", 2, 'd10', 1, 3),
               ("Halberd (2h)", 3, 'd10', 2, 3),
               ("War Hammer (2h)", 3, 'd10', 2, 3),
               ("Long Sword (2h)", 3, 'd10', 2, 3),
               ("Battle Axe (2h)", 3, 'd10', 2, 3),
               ("Sling", 1, 'd4', 1, 3),
               ("Bow (2h)", 2, 'd6', 2, 3),
               ("Crossbow (2h)", 3, 'd8', 2, 3)]
              ]

    armor = [Armor(name, slots, defense, quality) for (name, slots, defense, quality) in
             [['No armor', 1, 0, -1],
              ['No armor', 1, 0, -1],
              ['No armor', 1, 0, -1],
              ["Gambeson", 1, 1, 3],
              ["Gambeson", 1, 1, 3],
              ["Gambeson", 1, 1, 3],
              ["Gambeson", 1, 1, 3],
              ["Gambeson", 1, 1, 3],
              ["Gambeson", 1, 1, 3],
              ["Gambeson", 1, 1, 3],
              ["Gambeson", 1, 1, 3],
              ["Gambeson", 1, 1, 3],
              ["Gambeson", 1, 1, 3],
              ["Gambeson", 1, 1, 3],
              ["Brigandine", 2, 2, 4],
              ["Brigandine", 2, 2, 4],
              ["Brigandine", 2, 2, 4],
              ["Brigandine", 2, 2, 4],
              ["Brigandine", 2, 2, 4],
              ["Chain", 3, 4, 5]]
             ]

    # (Armor name, +defense, slots)
    helmet_shield = [
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [Armor("Helmet", 1, 1, 1)],
                     [Armor("Helmet", 1, 1, 1)],
                     [Armor("Helmet", 1, 1, 1)],
                     [Armor("Shield", 1, 1, 1)],
                     [Armor("Shield", 1, 1, 1)],
                     [Armor("Shield", 1, 1, 1)],
                     [Armor("Shield", 1, 1, 1), Armor("Helmet", 1, 1, 1)]]

    dungeon_gear = [Gear(item) for item in
                    ["Rope, 50ft",
                     "Pulleys",
                     "Candles, 5",
                     "Chain, 10ft",
                     "Chalk, 10",
                     "Crowbar",
                     "Tinderbox",
                     "Grap. hook",
                     "Hammer",
                     "Waterskin",
                     "Lantern",
                     "Lamp oil",
                     "Padlock",
                     "Manacles",
                     "Mirror",
                     "Pole, 10ft",
                     "Sack",
                     "Tent",
                     "Spikes, 5",
                     "Torch, 5"]
                    ]

    general_gear_1 = [Gear(item) for item in
                      ["Air bladder",
                       "Bear trap",
                       "Shovel",
                       "Bellows",
                       "Grease",
                       "Saw",
                       "Bucket",
                       "Caltrops",
                       "Chisel",
                       "Drill",
                       "Fish. rod",
                       "Marbles",
                       "Glue",
                       "Pick",
                       "Hourglass",
                       "Net",
                       "Tongs",
                       "Lockpicks",
                       "Metal file",
                       "Nails"]
                      ]

    general_gear_2 = [Gear(item) for item in
                      ["Incense"
                       "Sponge"
                       "Lens"
                       "Perfume"
                       "Horn"
                       "Bottle"
                       "Soap"
                       "Spyglass"
                       "Tar pot"
                       "Twine"
                       "Fake jewels"
                       "Blank book"
                       "Card deck"
                       "Dice set"
                       "Cook pots"
                       "Face paint"
                       "Whistle"
                       "Instrument"
                       "Quill & Ink"
                       "Small bell"]
                      ]
