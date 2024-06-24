# Much room for improvement but this works
# Could do more in memory

from Main import *
from helpers import *
from builtz.built import *


def plant_dinosaur(dinosaures, dinosaur_by_size, dir_):
    use_item(Items.Egg)
    dinosaur_size = measure()
    dinosaures[get_pos()] = dinosaur_size
    # dinosaur_by_size[size] = pos
    move(dir_)

def check_dinosaur(dinosaures, dir_):
    swapped = False
    pos = get_pos()
    for check_dir in all_directions:
        check_pos, change, new = get_pos_dir_and_value(pos, check_dir)
        if new < 0 or new > size_min_1:
            continue
        diff = dinosaures[check_pos] - dinosaures[pos]
        if (change > 0 and diff < 0) or (change < 0 and diff > 0):
            swapped = True
            swap(check_dir)
            dinosaures[pos], dinosaures[check_pos] = dinosaures[check_pos], dinosaures[pos]
    move(dir_)
    return swapped


def dinosaur(laps):
    buy_items(Items.Egg, squares_n * laps)

    for i in range(laps):

        dinosaures = {}
        dinosaur_by_size = {}

        for i2 in range(size):
            for i3 in range(size_min_1):
                if not i:
                    till()
                plant_dinosaur(dinosaures, dinosaur_by_size, East)
            if not i:
                till()
            plant_dinosaur(dinosaures, dinosaur_by_size, North)

        exit()
        # swapped = True
        # while swapped:
        #     swapped = False
        #     for i2 in range(size):
        #         for i3 in range(size_min_1):
        #             if check_dinosaur(dinosaures, East):
        #                 swapped = True
        #         if check_dinosaur(dinosaures, North):
        #             swapped = True
        # harvest()


