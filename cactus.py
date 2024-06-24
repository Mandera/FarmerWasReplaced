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


def move_cactus(target, cactuses, cactus_by_size):
    pos = get_pos()
    instructions = get_move_instructions_no_wrap(pos, target)
    for instruction in instructions:
        dir_, move_n = instruction
        for x in range(move_n):
            new_pos = get_pos_dir(pos, dir_)
            switch_cactus_and_follow(pos, new_pos, dir_, cactuses, cactus_by_size)
            pos = new_pos


# 491115 start
# 429488 first working iteration of moving deliberately

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
                target = pos_from_index(len(done_cactus))
                move_cactus(target, cactuses, cactus_by_size)
                positions.remove(target)
                done_cactus.append(target)


        # while True:
        #     if check_if_should_harvest(cactuses):
        #         harvest()
        #         break

        harvest()

        print(get_op_count() - start)

        exit()






