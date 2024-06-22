# Much room for improvement but this works
# Could do more in memory

from Main import *
from helpers import *
from builtz.built import *


def pumpkin_harvest(direction, check_coords):
    if get_entity_type() == None:
        plant(Entities.Pumpkin)
        check_coords.append(get_pos())
    move(direction)


def plant_cactus(cactuses, cactus_by_size, dir_):
    plant(Entities.Cactus)
    cactus_size = measure()
    cactuses[get_pos()] = cactus_size
    # cactus_by_size[size] = pos
    move(dir_)

def check_cactus(cactuses, dir_):
    swapped = False
    pos = get_pos()
    for check_dir in all_directions:
        check_pos, change, new = get_pos_dir_and_value(pos, check_dir)
        if new < 0 or new > size_min_1:
            continue
        diff = cactuses[check_pos] - cactuses[pos]
        if (change > 0 and diff < 0) or (change < 0 and diff > 0):
            swapped = True
            swap(check_dir)
            cactuses[pos], cactuses[check_pos] = cactuses[check_pos], cactuses[pos]
    move(dir_)
    return swapped


def cactus(laps):
    buy_items(Items.Cactus_Seed, squares_n * laps)

    for i in range(laps):

        cactuses = {}
        cactus_by_size = {}

        for i2 in range(size):
            for i3 in range(size_min_1):
                if not i:
                    till()
                plant_cactus(cactuses, cactus_by_size, East)
            if not i:
                till()
            plant_cactus(cactuses, cactus_by_size, North)

        swapped = True
        while swapped:
            swapped = False
            for i2 in range(size):
                for i3 in range(size_min_1):
                    if check_cactus(cactuses, East):
                        swapped = True
                if check_cactus(cactuses, North):
                    swapped = True
        harvest()


