from exceptions import InventoryFullException


class Inventory(object):
    def __init__(self, character):
        self._inventory = []
        self.character = character

    @property
    def armor_defense(self):
        return 11 + sum([item.defense for item in self._inventory
                         if (item.type == 'Armor' and item.equipped)])

    @property
    def total_slots(self):
        return self.character.stats['constitution'] + 10

    @property
    def used_slots(self):
        return sum([item.slots for item in self._inventory])

    @property
    def slots(self):
        return (self.used_slots, self.total_slots)

    def add(self, item, equip=False):
        if item is None:
            return
        if isinstance(item, list):
            for each in item:
                self._add(each, equip)
        else:
            self._add(item, equip)

    def _add(self, item, equip):
        if item.name == 'No armor':
            return
        if self.used_slots + item.slots > self.total_slots:
            raise InventoryFullException
        if equip:
            item.equip()
            if item.type == 'Weapon':
                [xitem.unequip() for xitem in self._inventory if xitem.type == 'Weapon']
                if item.hands == 2:
                    # Unequip shields
                    [xitem.unequip() for xitem in self._inventory if xitem.name == 'Shield']
            if item.type == 'Armor':
                if item.name == 'Shield':
                    [xitem.unequip() for xitem in self._inventory if xitem.name == item.name]
                    # Unequip 2 handed weapons
                    [xitem.unequip() for xitem in self._inventory
                     if (xitem.type == 'Weapon') and (xitem.hands == 2)]
                elif item.name == 'Helmet':
                    [xitem.unequip() for xitem in self._inventory if xitem.name == item.name]
                else:
                    [xitem.unequip() for xitem in self._inventory
                     if (xitem.name not in ['Shield', 'Helmet'])
                     and (xitem.type == item.type)]
        self._inventory.append(item)

    def __str__(self):
        format_string = "{0: <25}{1: <10}{2:^15}"
        inventory_strings = []
        inventory_strings.append("-"*50)
        for item in self.sorted():
            if item.equipped:
                name = '* %s' % item.name
            else:
                name = item.name
            inventory_strings.append(format_string.format(name, item.type, str(item.slots)))
        inventory_strings.insert(0, format_string
                                 .format("Item", "Type", "Slots %s/%s" % self.slots))
        return "\n".join(inventory_strings)

    def sorted(self):
        return sorted(self._inventory, key=self.format_priority)

    def format_priority(self, item):
        return ['Weapon', 'Armor', 'Gear', 'Food'].index(item.type)

    def delete_all(self):
        self._inventory = []
