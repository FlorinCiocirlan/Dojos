inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(x):
    for i in x:
        print(i, ":", x[i])


dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def add_inventory(invent, added_items):
    for a in added_items:
        if a in invent:
            invent[a] += 1
        else:
            invent[a] = 1
        return invent

order = 0
def print_table(inventory, order):
    order = input("How do you want to show the table ?")
    max_len = 0
    for i in inventory:
        if len(i) > max_len:
            max_len = len(i)

    if "count,asc" in order:
        for i in sorted(inventory, key=inventory.get):
            print(str(i).rjust(max_len), "|", str(inventory[i]).rjust(4))


    elif "count,desc" in order:
        for i in sorted(inventory, key=inventory.get, reverse=True):
            print(str(i).rjust(max_len), "|", str(inventory[i]).rjust(4))


    else:
        for i in inventory:
            print(str(i).rjust(max_len), "|", str(inventory[i]).rjust(4))

add_inventory(inv, dragon_loot)
print_table(inv, order)
