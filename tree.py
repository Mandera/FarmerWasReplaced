from Main import size, diagonals
from builtz.built import harvest, till, plant, Entities, move, East, North, can_harvest


def do_tree(i, direction):
    if i:
        harvest()
    else:
        till()
    plant(Entities.Tree)
    # use_item(Items.Water_Tank)
    move(East)
    move(direction)


def tree(laps):
    for i in range(laps):
        for x in range(size):
            for y in range(diagonals):
                do_tree(i, East)
            do_tree(i, North)
        while not can_harvest():
            pass
