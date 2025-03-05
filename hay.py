from Main import size, size_min_1
from __builtins__ import *


def hay(laps, setup=True):
    till()

    for i in range(laps):
        for x in range(size):
            if x:
                harvest()
            else:
                while not can_harvest() and i:
                    pass
                harvest()
                plant(Entities.Sunflower)
                use_item(Items.Water)
            move(North)
            for y in range(size_min_1):
                harvest()
                move(East)
