
def create_inventory(items):
    inventory = dict()
    set_of_items = set(items)
    for n in set_of_items:
        v = items.count(n)
        inventory[n] = v
    return inventory

def add_items(inventory,items):
    set_of_items = set(items)
    for n in set_of_items:
        v = items.count(n)
        if n in inventory:
            inventory[n] = inventory[n]+v 
        else:
            inventory[n] = v
    return inventory

def decrement_items(inventory,items):
    set_of_items = set(items)
    for n in set_of_items:
        count_in_items = items.count(n)
        if inventory[n]<count_in_items:
            inventory[n] = 0
        else:
            inventory[n] = inventory[n]-count_in_items
    return inventory

def remove_item(inventory,item):
    if item in inventory:
        del inventory[item]
    return inventory

def list_inventory(inventory):
    list_ = []
    for key,value in inventory.items():
        if value > 0:
            a = (key,value)
            list_.append(a)
    return list_ 
