# Much room for improvement but this works
# Could do more in memory

from Main import *
from helpers import *
from builtz.built import *


def plant_cactus(cactus_by_size, dir_):
    plant(Entities.Cactus)
    cactus_size = measure()
    pos = get_pos()
    cactus_by_size[cactus_size].append(pos)
    move(dir_)


def switch_cactus_and_follow(pos, new_pos, dir_, cactus_size, cactus_by_size):
    swap(dir_)

    other_cactus_size = measure()

    cactus_by_size[cactus_size].remove(pos)
    cactus_by_size[cactus_size].append(new_pos)
    cactus_by_size[other_cactus_size].remove(new_pos)
    cactus_by_size[other_cactus_size].append(pos)

    move(dir_)
    return new_pos


def move_cactus(target, cactus_by_size, cactus_size):
    pos = get_pos()

    cactus_by_size[cactus_size].remove(pos)

    instructions = get_move_instructions_no_wrap(pos, target)
    for instruction in instructions:
        dir_, move_n = instruction
        for x in range(move_n):
            new_pos = get_pos_dir(pos, dir_)
            swap(dir_)
            other_cactus_size = measure()

            cactus_by_size[other_cactus_size].remove(new_pos)
            cactus_by_size[other_cactus_size].append(pos)

            move(dir_)
            pos = new_pos



# 491115 start
# 429488 first working iteration of moving deliberately
# 431168 first attempt at improving
# 404707 start with last index
# 400401 remove moved cactus from dict right away


# Start top right
def pos_from_index(index):
    x = size - index % size - 1
    y = size - index // size - 1
    return x, y


def cactus(laps):
    buy_items(Items.Cactus_Seed, squares_n * laps)

    for i in range(laps):
        start = get_op_count()
        cactus_by_size = {}
        done_cactus = 0

        for i2 in range(10):
            cactus_by_size[i2] = []

        for i2 in range(size):
            for i3 in range(size_min_1):
                if not i:
                    till()
                plant_cactus(cactus_by_size, East)
            if not i:
                till()
            plant_cactus(cactus_by_size, North)


        for cactus_size_i in range(10):
            cactus_size = 9 - cactus_size_i
            positions = cactus_by_size[cactus_size]

            for i2 in range(len(positions)):
                goto(positions[-1])
                target = pos_from_index(done_cactus)
                move_cactus(target, cactus_by_size, cactus_size)
                done_cactus += 1

        harvest()

        print(get_op_count() - start)

        exit()






