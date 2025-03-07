
from __builtins__ import *
from Main import *


def carrot(laps, setup=True):
    if setup:
        for x in range(size):
            for y in range(size_min_1):
                till()
                move(East)
            till()
            move(North)

    for i in range(laps):
        for x in range(size):
            for y in range(size_min_1):
                carrot_harvest(Entities.Carrot, East)
            if x:
                carrot_harvest(Entities.Carrot, North)
            else:
                carrot_harvest(Entities.Sunflower, North)

        while not can_harvest():
            pass


def carrot_harvest(seed, direction):
    harvest()
    plant(seed)
    use_item(Items.Water)
    move(direction)



