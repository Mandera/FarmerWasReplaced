

from Main import *


# This will be True, avoid it
# 0 == False
# 1 == True

# Squares:
# None if unvisited
# True if visited

# Walls
# None if untested
# OPEN if open
# teleport_i if wall


def start_maze():
    plant(Entities.Bush)
    while get_entity_type() == Entities.Bush:
        use_item(Items.Fertilizer)

def pos_key_wall(pos, dir_=None):
    # ("h", 1, 3) or ("v", 6, 2)
    if dir_ in direction_wall_offset:
        pos = list(pos)
        i, value = direction_wall_offset[dir_]
        pos[i] += value
    return direction_prefix[dir_] + (pos[0], pos[1])

def get_wall(pos, dir_):
    key = pos_key_wall(pos, dir_)
    if key in glob["walls"]:
        return glob["walls"][key]

def set_wall(pos, dir_, value):
    key = pos_key_wall(pos, dir_)
    glob["walls"][key] = value

def get_square(pos):
    if pos in glob["squares"]:
        return glob["squares"][pos]

def set_square(pos, value):
    glob["squares"][pos] = value

def measure_pos():
    x, y = measure()
    return x, y

def check_treasure():
    do_measure = True
    while get_entity_type() == Entities.Treasure:
        if glob["teleport_i"] == glob["teleports"]:
            harvest()
            return True

        if do_measure:
            glob["treasure_pos"] = measure_pos()

            if glob["treasure_pos"] != glob["pos"]:
                glob["teleport_i"] += 1
                do_measure = False
                # HERE ** Force edge case if we want by resetting squares and walls
                # reset_grid()
        use_item(Items.Fertilizer)

# Return new unclamped pos
def new_pos(pos, dir_):
    i, value = direction_numbers[dir_]
    pos2 = list(pos)
    pos2[i] = pos2[i] + value
    return pos2[0], pos2[1]

# Return new clamped pos
def new_pos_contain(pos, dir_):
    i, value = direction_numbers[dir_]
    pos2 = list(pos)
    pos2[i] = (pos2[i] + value) % size
    return pos2[0], pos2[1]



def tracked_move(dir_):
    result = move(dir_)
    if result:
        glob["pos"] = new_pos_contain(glob["pos"], dir_)
    return result

def try_move_dir(dir_):
    # Already tried going through here, see if we should skip
    wall = get_wall(glob["pos"], dir_)

    # Always skip wall
    if wall != OPEN and wall != None and wall >= 0:
        return False

    # Already been to target square
    target_pos = new_pos(glob["pos"], dir_)
    if get_square(target_pos):
        return False

    # Successfully moved
    if move(dir_):
        set_wall(glob["pos"], dir_, OPEN)
        glob["pos"] = new_pos(glob["pos"], dir_)
        set_square(glob["pos"], True)
        return True

    # There's a wall
    set_wall(glob["pos"], dir_, glob["teleport_i"])
    return False


# Used when target has not been explored yet
# Goal is to touch untouched squares
def explore_one_square():
    for dir_i in range(2):
        directions = direction_indexes[dir_i]
        for dir_ in directions:
            if try_move_dir(dir_):
                return True
    # Dead-end, enable back track
    # glob["back_track"] = True

def pathfind(pos):
    print("pathfind", pos)
    do_a_flip()
    pass

def square_is_explored(pos):
    for dir_ in all_directions:
        if get_wall(pos, dir_) == None:
            return False
    return True

def closest_unexplored_square():
    for square in glob["squares"]:
        if not square_is_explored(square):
            return square

def reset_grid():
    glob["pos"] = get_pos()
    glob["squares"] = {}
    glob["walls"] = {}
    glob["squares"][glob["pos"]] = True

# Bug: If a wall disappears in unsearched squares_n it can get stuck
def maze(laps):
    for lap in range(laps):
        reset_grid()

        glob["teleports"] = 100  # Max is 299, but I think there's an edge case where it teleports to same square twice and will be undetectable
        glob["teleport_i"] = 0
        glob["back_track"] = False
        glob["treasure_pos"] = None

        start_maze()

        while True:
            if check_treasure():
                # Chest was harvested
                break


            if glob["treasure_pos"] and get_square(glob["treasure_pos"]):
                pathfind(glob["treasure_pos"])

            if not explore_one_square():
                pathfind(closest_unexplored_square())

            # make_move()

            # if not glob["treasure_pos"]:
            #     make_move()
            #
            # elif not glob["treasure_grid_pos"]:
            #     make_move()
            #
            # else:
            #     quick_print("treasure found and discovered")
            #     while True:
            #         do_a_flip()






