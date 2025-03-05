
from Main import *
from __builtins__ import *


def do_tree(i, direction):
    if i:
        harvest()
    else:
        till()
    plant(Entities.Tree)
    use_item(Items.Water)
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
