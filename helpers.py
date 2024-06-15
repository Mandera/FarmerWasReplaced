
from builtz.built import *
from Main import *


def bool_to_int(boolean):
    if boolean:
        return 1
    return 0

def buy_items(item, target):
    current = num_items(item)
    if current < target:
        trade(item, target - current)

def get_pos():
    return get_pos_x(), get_pos_y()

# Returns 0 if n1 should increase or 1 if n1 should decrease for quickest navigation
# size = 10
# 3, 4 -> 0, 1
# 5, 2 -> 1, 3
# 8, 2 -> 0, 4

def move_instructions(n1, n2):
    diff = n2 - n1
    abs_diff = abs(diff)

    if abs_diff <= half_size:
        return bool_to_int(diff > 0), abs_diff
    else:
        if diff < 0:
            return 0, diff + size
        else:
            return 1, size - abs_diff

def move_multi(direction, amount):
    for n in range(amount):
        move(direction)

def goto(target):
    pos = get_pos()
    for i in range(2):
        n1 = pos[i]
        n2 = target[i]
        if n1 != n2:
            move_i, move_n = move_instructions(n1, n2)
            move_multi(direction_indexes[i][move_i], move_n)


