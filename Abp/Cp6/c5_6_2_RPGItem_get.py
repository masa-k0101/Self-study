# -*- coding: utf-8 -*-

from c5_6_1_RPGItem import display_inventory

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[imte] + 1
    return inventory

if __name__ == "__main__":
    inv = {'coin':42, 'lope':1}
    dragon_loot = {'coin', 'knife', 'coin', 'coin','jewel'}
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)