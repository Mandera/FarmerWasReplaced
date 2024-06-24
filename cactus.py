# Much room for improvement but this works
# Could do more in memory

from Main import *
from helpers import *
from builtz.built import *


def plant_cactus(cactuses, cactus_by_size, dir_):
    plant(Entities.Cactus)
    cactus_size = measure()
    pos = get_pos()
    cactuses[pos] = cactus_size
    cactus_by_size[cactus_size].append(pos)
    move(dir_)

def switch_cactus_and_follow(pos, new_pos, dir_, cactuses, cactus_by_size):
    swap(dir_)
    pos_size = cactuses[pos]
    new_pos_size = cactuses[new_pos]
    cactuses[pos], cactuses[new_pos] = new_pos_size, pos_size

    cactus_by_size[pos_size].remove(pos)
    cactus_by_size[pos_size].append(new_pos)
    cactus_by_size[new_pos_size].remove(new_pos)
    cactus_by_size[new_pos_size].append(pos)

    move(dir_)
    return new_pos

# This doesnt work cus it might get stuck
def put_cactus_in_good_place(cactuses, cactus_by_size, moved=False):
    pos = get_pos()
    for check_dir in all_directions:
        check_pos, change, new = get_pos_dir_and_value(pos, check_dir)

        # Outside map
        if new < 0 or new > size_min_1:
            continue

        pos_size = cactuses[pos]
        check_size = cactuses[check_pos]

        diff = check_size - pos_size
        if (change > 0 and diff < 0) or (change < 0 and diff > 0):
            switch_cactus_and_follow(pos, check_pos, check_dir, cactuses, cactus_by_size)
            return put_cactus_in_good_place(cactuses, cactus_by_size, True)
    return moved


def move_cactus(target, cactuses, cactus_by_size):
    pos = get_pos()
    for instruction in get_move_instructions_no_wrap(pos, target):
        dir_, move_n = instruction
        for x in range(move_n):
            new_pos = get_pos_dir(pos, dir_)
            switch_cactus_and_follow(pos, new_pos, dir_, cactuses, cactus_by_size)
            pos = new_pos


# 491115 start


# Start top right
def pos_from_index(index):
    x = size - index % size - 1
    y = size - index // size - 1
    return x, y


def cactus(laps):
    buy_items(Items.Cactus_Seed, squares_n * laps)

    for i in range(laps):
        start = get_op_count()
        cactuses = {}
        cactus_by_size = {}
        done_cactus = []

        for i2 in range(10):
            cactus_by_size[i2] = []

        for i2 in range(size):
            for i3 in range(size_min_1):
                if not i:
                    till()
                plant_cactus(cactuses, cactus_by_size, East)
            if not i:
                till()
            plant_cactus(cactuses, cactus_by_size, North)



        # set_execution_speed(2)
        # check_if_should_harvest(cactuses)
        # check_and_follow(cactuses)


        for cactus_size_i in range(10):
            cactus_size = 9 - cactus_size_i
            positions = cactus_by_size[cactus_size]

            while positions:
                goto(positions[0])
                put_cactus_in_good_place(cactuses, cactus_by_size)
                positions.remove(get_pos())


        # while True:
        #     if check_if_should_harvest(cactuses):
        #         harvest()
        #         break

        harvest()

        print(get_op_count() - start)

        exit()






# Old

def check_if_should_harvest(cactuses):
    should_harvest = True
    for i2 in range(size):
        for i3 in range(size_min_1):
            if check_cactus(cactuses):
                should_harvest = False
            move(East)
        if check_cactus(cactuses):
            should_harvest = False
        move(North)
    return should_harvest



def check_cactus(cactuses):
    swapped = False
    pos = get_pos()
    for check_dir in all_directions:
        check_pos, change, new = get_pos_dir_and_value(pos, check_dir)

        # Outside map
        if new < 0 or new > size_min_1:
            continue

        diff = cactuses[check_pos] - cactuses[pos]
        if (change > 0 and diff < 0) or (change < 0 and diff > 0):
            swapped = True
            swap(check_dir)
            cactuses[pos], cactuses[check_pos] = cactuses[check_pos], cactuses[pos]
    return swapped

def check_and_follow(cactuses):
    for i2 in range(size):
        for i3 in range(size_min_1):
            if put_cactus_in_good_place(cactuses):
                return  # Start over
            move(East)
        if put_cactus_in_good_place(cactuses):
            return
        move(North)




