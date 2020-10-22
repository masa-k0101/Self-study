# -*- coding: utf-8 -*-

def display_inventory(inventory):
    print('Item list:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print("Numbers of item: " + str(item_total))

if __name__ == "__main__":
    Kirito = {'lope':1, 'torch':6, 'coin':42, 'bow':1, 'allow':12}
    display_inventory(Kirito)
