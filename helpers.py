
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




def move_instructions_with_wrap(n1, n2):
    diff = n2 - n1
    abs_diff = abs(diff)

    # Go Direct
    if abs_diff <= half_size:
        return bool_to_int(diff < 0), abs_diff
    else:
        if diff < 0:
            return 0, diff + size
        else:
            return 1, size - diff

def move_multi(direction, amount):
    for n in range(amount):
        move(direction)

def goto(target):
    pos = get_pos()
    for i in range(2):
        n1 = pos[i]
        n2 = target[i]
        if n1 != n2:
            move_i, move_n = move_instructions_with_wrap(n1, n2)
            move_multi(direction_indexes[i][move_i], move_n)


def move_instructions_no_wrap(n1, n2):
    diff = n2 - n1
    abs_diff = abs(diff)
    return bool_to_int(diff < 0), abs_diff

def get_move_instructions_no_wrap(pos, target):
    instructions = []
    for i in range(2):
        n1 = pos[i]
        n2 = target[i]
        if n1 != n2:
            move_i, move_n = move_instructions_no_wrap(n1, n2)
            dir_ = direction_indexes[i][move_i]
            instructions.append((dir_, move_n))
    return instructions







# Return new unclamped pos
def get_pos_dir(pos, dir_):
    i, value = direction_numbers[dir_]
    pos2 = list(pos)
    pos2[i] = pos2[i] + value
    return pos2[0], pos2[1]


def get_pos_dir_and_value(pos, dir_):
    i, change = direction_numbers[dir_]
    pos2 = list(pos)
    new = pos2[i] + change
    pos2[i] = new
    return (pos2[0], pos2[1]), change, new



