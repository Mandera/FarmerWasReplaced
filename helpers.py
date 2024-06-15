
from Main import *


def buy_items(item, target):
    current = num_items(item)
    if current < target:
        trade(item, target - current)

def get_pos():
    return get_pos_x(), get_pos_y()

# Returns 0 if n1 should increase or 1 if n1 should decrease for quickest navigation
def move_instructions(n1, n2):
    diff = n2 - n1
    abs_diff = abs(diff)

    if abs_diff <= half_size:
        return int(diff > 0), abs_diff
    else:
        return int(diff < 0), abs_diff - half_size

def move_multi(direction, amount):
    for n in amount:
        move(direction)

def goto(target):
    pos = get_pos()
    for i in range(2):
        n1 = pos[i]
        n2 = target[i]
        if n1 != n2:
            move_i, move_n = move_instructions(n1, n2)
            move_multi(direction_indexes[i][move_i], move_n)


