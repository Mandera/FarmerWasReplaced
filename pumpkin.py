
from Main import *
from helpers import *
from __builtins__ import *


def pumpkin_harvest(direction, check_coords):
    if get_entity_type() == None:
        plant(Entities.Pumpkin)
        check_coords.append(get_pos())
    move(direction)


def pumpkins(laps):

    for i in range(laps):
        for i2 in range(size):
            for i3 in range(size_min_1):
                if not i:
                    till()
                plant(Entities.Pumpkin)
                move(East)
            if not i:
                till()
            plant(Entities.Pumpkin)
            move(North)

        do_a_flip()
        do_a_flip()
        do_a_flip()

        check_coords = []
        for i2 in range(size):
            for i3 in range(size_min_1):
                pumpkin_harvest(East, check_coords)
            pumpkin_harvest(North, check_coords)

        for coords in check_coords:
            goto(coords)
            while True:
                if get_entity_type() == None:
                    plant(Entities.Pumpkin)
                if not can_harvest():
                    use_item(Items.Fertilizer)
                if can_harvest():
                    break


        do_a_flip()
        do_a_flip()
        do_a_flip()

        harvest()


