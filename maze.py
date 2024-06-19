

from Main import *


# This will be True, avoid it
# 0 == False
# 1 == True


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

# None if untested
# OPEN if open
# teleport_i if wall
def get_wall(pos, dir_):
    key = pos_key_wall(pos, dir_)
    if key in glob["walls"]:
        return glob["walls"][key]

def set_wall(pos, dir_, value):
    key = pos_key_wall(pos, dir_)
    glob["walls"][key] = value

# None if unvisited
# True if visited
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
                reset_grid()
        use_item(Items.Fertilizer)

# Return new unclamped pos
def get_pos_dir(pos, dir_):
    i, value = direction_numbers[dir_]
    pos2 = list(pos)
    pos2[i] = pos2[i] + value
    return pos2[0], pos2[1]

# Return new clamped pos
def get_pos_dir_contain(pos, dir_):
    i, value = direction_numbers[dir_]
    pos2 = list(pos)
    pos2[i] = (pos2[i] + value) % size
    return pos2[0], pos2[1]

# def tracked_move(dir_):
#     result = move(dir_)
#     if result:
#         glob["pos"] = get_pos_dir_contain(glob["pos"], dir_)
#     return result

def should_explore_dir_check(dir_):
    wall = get_wall(glob["pos"], dir_)
    if wall == None:
        return True  # Try unexplored
    if wall == OPEN:
        return False  # Already know it's open
    return False

def try_explore_dir(dir_):
    if should_explore_dir_check(dir_):
        if move(dir_):
            set_wall(glob["pos"], dir_, OPEN)
            glob["pos"] = get_pos_dir(glob["pos"], dir_)
            set_square(glob["pos"], True)
            return True
        else:
            set_wall(glob["pos"], dir_, glob["teleport_i"])
    return False

# Used when target has not been explored yet
# Goal is to touch untouched squares
# Todo: Ensure it choses the closest one, perhaps use part of the pathfinding code
def explore_one_square():
    for dir_i in range(2):
        directions = direction_indexes[dir_i]
        for dir_ in directions:
            if try_explore_dir(dir_):
                return True

# Return a list of squares and dirs_ that we know are open to the given pos
def open_squares(pos):
    squares_and_dir = []
    for dir_ in all_directions:
        wall = get_wall(pos, dir_)
        if wall == OPEN:
            target_square = get_pos_dir(pos, dir_)
            squares_and_dir.append((target_square, dir_))
    return squares_and_dir


# pathfind in memory, returns dict of directions
# For every found square, we put the reversed direction on it

def pathfind_directions(from_pos, to_pos):
    square_directions = {to_pos: None}
    next_round_squares = set()
    while True:
        if len(square_directions) == 1:
            check_squares = {to_pos}
        else:
            check_squares = next_round_squares

        next_round_squares = set()
        for check_square in check_squares:
            for values in open_squares(check_square):
                new_square, dir_ = values
                if check_square == new_square:
                    continue
                if new_square in square_directions:
                    continue

                # This is a new square
                opposite_dir = direction_opposite[dir_]
                next_round_squares.add(new_square)
                square_directions[new_square] = opposite_dir

                # Done
                if new_square == from_pos:
                    return square_directions


def pathfind(to_pos):
    pos = get_pos()
    square_directions = pathfind_directions(pos, to_pos)

    while pos != to_pos:
        dir_ = square_directions[pos]
        move(dir_)
        pos = get_pos_dir(pos, dir_)
    glob["pos"] = pos

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
            harvested_treasure = check_treasure()
            if harvested_treasure:
                break

            # We can pathfind directly to treasure
            if glob["treasure_pos"] and get_square(glob["treasure_pos"]):
                pathfind(glob["treasure_pos"])

            # Keep exploring
            else:
                moved = explore_one_square()
                if not moved:
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






