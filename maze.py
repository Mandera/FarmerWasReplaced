

from Main import *


def start_maze():
    plant(Entities.Bush)
    while get_entity_type() == Entities.Bush:
        use_item(Items.Fertilizer)


def blank_grid():
    grid = {}
    # grid = {"squares": {}, "h_wall": {}, "v_wall": {}}

    # for x in range(size):
    #     grid[x] = {}
    #     for y in range(size):
    #         grid[x][y] = {}
    return grid


# This will be True, avoid it
# 0 == False
# 1 == True


def to_str(n):
    return num_to_str[n]

def pos_key(pos):
    return to_str(pos[0]) + "," + to_str(pos[1])

def pos_key_wall(pos, dir_=None):
    # h1,3 or v6,2
    if dir_ in direction_wall_offset:
        pos = list(pos)
        i, value = direction_wall_offset[dir_]
        pos[i] += value
    return direction_prefix[dir_] + pos_key(pos)


# None if unvisited
# True if visited
def get_square(pos):
    key = pos_key(pos)
    if key in glob["grid"]:
        return glob["grid"]

def set_square(pos, value):
    key = pos_key(pos)
    glob["grid"][key] = value


# None if untested
# OPEN if open
# teleport_i if wall
def get_wall(pos, dir_):
    key = pos_key_wall(pos, dir_)
    if key in glob["grid"]:
        return glob["grid"]

def set_wall(pos, dir_, value):
    key = pos_key_wall(pos, dir_)
    glob["grid"][key] = value


def measure_pos():
    x, y = measure()
    return [x, y]

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

                # set_execution_speed(0.5)
                # HERE ** Force edge case
                # glob["grid"] = blank_grid()
                # glob["grid_pos"] = get_grid_pos(glob["grid"], glob["pos"])
        use_item(Items.Fertilizer)


# def unexplored_positions():


# Updates clamped pos
def update_pos_contain(pos, dir_):
    i, value = direction_numbers[dir_]
    pos[i] = (pos[i] + value) % size

# Updates unclamped pos
def update_pos(pos, dir_):
    i, value = direction_numbers[dir_]
    pos[i] = (pos[i] + value)

# Return new unclamped pos
def new_pos(pos, dir_):
    i, value = direction_numbers[dir_]
    pos2 = list(pos)
    pos2[i] = pos2[i] + value
    return pos2

def tracked_move(dir_):
    result = move(dir_)
    if result:
        update_pos_contain(glob["pos"], dir_)
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
        update_pos(glob["pos"], dir_)
        set_square(glob["pos"], True)
        return True

    # There's a wall
    set_wall(glob["pos"], dir_, glob["teleport_i"])
    return False



# Used when target has not been explored yet
# Goal is to touch more squares
def explore():
    for dir_i in range(2):
        directions = direction_indexes[dir_i]
        for dir_ in directions:
            if try_move_dir(dir_):
                return True
    # Dead-end, enable back track
    # glob["back_track"] = True


# def pathfind():
#



# Bug: If a wall disappears in unsearched squares_n it can get stuck
def maze(laps):
    for lap in range(laps):
        glob["pos"] = get_pos()
        glob["grid"] = blank_grid()
        set_square(glob["pos"], True)
        glob["teleports"] = 100  # Max is 299, but I think there's an edge case where it teleports to same square twice and will be undetectable
        glob["teleport_i"] = 0
        glob["back_track"] = False
        glob["treasure_pos"] = None

        start_maze()

        while True:
            if check_treasure():
                # Chest was harvested
                break

            explore()

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






