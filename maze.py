
from Main import *
from helpers import *
from __builtins__ import *


# This will be True, avoid it
# 0 == False
# 1 == True


def start_maze():
    plant(Entities.Bush)
    while get_entity_type() == Entities.Bush:  # HERE ** seems you dont do this anymore
        use_item(Items.Fertilizer)

def reset_walls():
    glob["walls"] = {}
    for i in range(2):
        y = i * size
        for i2 in range(size):
            glob["walls"][("h", i2, y)] = OUTSIDE_WALL
            glob["walls"][("v", y, i2)] = OUTSIDE_WALL

def pos_key_wall(pos, dir_=None):
    # ("h", 1, 3) or ("v", 6, 2)
    if dir_ in direction_wall_offset:
        pos = list(pos)
        i, value = direction_wall_offset[dir_]
        pos[i] += value
    return direction_prefix[dir_] + (pos[0], pos[1])

# None if untested
# OPEN if open
# OUTSIDE_WALL if outside wall
# teleport_i if wall (check with >= 0)
def get_wall(pos, dir_):
    key = pos_key_wall(pos, dir_)
    if key in glob["walls"]:
        return glob["walls"][key]

def set_wall(pos, dir_, value):
    key = pos_key_wall(pos, dir_)
    glob["walls"][key] = value

# None if unvisited
# False if visited but not fully explored
# True if explored
def get_square(pos):
    if pos in glob["squares"]:
        return glob["squares"][pos]

def set_square(pos, value):
    glob["squares"][pos] = value

    if value:
        if pos in glob["unexplored"]:
            glob["unexplored"].remove(pos)
    else:
        if pos not in glob["unexplored"]:
            glob["unexplored"].append(pos)

def measure_pos():
    x, y = measure()
    return x, y

def fertilize_or_harvest_treasure():
    if glob["teleport_i"] == glob["teleports"]:
        print("ops", get_tick_count() - glob["start_ops"])
        harvest()
        return True

    treasure_pos = measure_pos()
    while not use_item(Items.Fertilizer):
        pass

    # reset_grid()  # Encourage edge case

    glob["teleport_i"] += 1
    if treasure_pos == glob["pos"]:
        return fertilize_or_harvest_treasure()
    else:
        glob["treasure_pos"] = treasure_pos

def check_treasure():
    if get_entity_type() == Entities.Treasure:
        return fertilize_or_harvest_treasure()


def should_explore_dir_check(dir_):
    wall = get_wall(glob["pos"], dir_)
    if wall == None:
        return True  # Try unexplored
    if wall == OPEN:
        return False  # Already know it's open
    return False  # index (wall) or OUTSIDE_WALL

def try_explore_dir(pos, dir_):
    new_pos = get_pos_dir(pos, dir_)  # Regardless if moved or not we have the potential new pos
    moved = move(dir_)
    if moved:
        set_wall(pos, dir_, OPEN)
        set_square(new_pos, False)  # It's possible that the new pos is now fully explored but disregard that
        glob["pos"] = new_pos
    else:
        i = glob["teleport_i"]
        set_wall(pos, dir_, i)

        i2 = TELEPORTS_UNTIL_RECHECK_WALL + i
        glob["squares_with_walls"][pos] = i2
        glob["squares_with_walls"][new_pos] = i2
    return moved, new_pos


def square_has_wall(pos):
    for dir_ in all_directions:
        wall = get_wall(pos, dir_)
        if wall != OPEN and wall != OUTSIDE_WALL:
            return True

# Physically check all walls surrounding a square
def check_old_walls(cur_pos):
    i = glob["teleport_i"]
    if cur_pos not in glob["squares_with_walls"] or glob["squares_with_walls"][cur_pos] > i:
        return False

    walls_gone = False

    for dir_ in all_directions:
        wall = get_wall(cur_pos, dir_)
        if wall != OPEN and wall != OUTSIDE_WALL:
            if move(dir_):
                # quick_print("found deleted wall!", cur_pos, dir_)

                new_pos = get_pos_dir(cur_pos, dir_)
                move(direction_opposite[dir_])
                if get_square(new_pos) == None:
                    set_square(new_pos, False)
                set_wall(cur_pos, dir_, OPEN)

                # quick_print("there are now", len(glob["squares_with_walls"]), "squares with walls")

                if new_pos in glob["squares_with_walls"] and not square_has_wall(new_pos):
                    glob["squares_with_walls"].pop(new_pos)

                if not square_has_wall(cur_pos):
                    glob["squares_with_walls"].pop(cur_pos)
                    walls_gone = True
                    break
            else:
                set_wall(cur_pos, dir_, i)

    if not walls_gone:
        glob["squares_with_walls"][cur_pos] = i


# Used when target has not been explored yet
# Goal is to touch untouched squares
# True if moved
def explore_one_square():
    moved = False
    start_pos = glob["pos"]
    for dir_ in all_directions:
        if not should_explore_dir_check(dir_):
            continue
        moved, new_pos = try_explore_dir(start_pos, dir_)
        if moved:
            break

    if dir_ == last_dir:  # Fully explored
        set_square(start_pos, True)
    else:
        set_square(start_pos, False)

    return moved

# Breadth first pathfind in memory, returns dict of directions
# For every found square, we put the reversed direction on it, and because of that we start from to_pos
def pathfind_directions(from_pos, to_pos):
    square_directions = {from_pos: None}
    check_squares = {from_pos}

    while True:
        next_round_squares = set()

        for check_square in check_squares:
            if len(square_directions) > 1:
                directions = square_directions[check_square]
                dir_ = directions[-1]
            else:
                directions = ()
                dir_ = None

            for new_dir in direction_explore[dir_]:
                if get_wall(check_square, new_dir) != OPEN:
                    continue

                new_square = get_pos_dir(check_square, new_dir)

                if new_square in square_directions:
                    continue

                square_directions[new_square] = directions + (new_dir, )

                # Done
                if new_square == to_pos:
                    return square_directions[new_square]

                next_round_squares.add(new_square)
        check_squares = next_round_squares

def pathfind(to_pos):
    pos = glob["pos"]
    square_directions = pathfind_directions(pos, to_pos)

    for dir_ in square_directions:
        check_old_walls(pos)
        move(dir_)
        pos = get_pos_dir(pos, dir_)
    glob["pos"] = pos

def reset_grid():
    glob["pos"] = get_pos()
    glob["squares_with_walls"] = {}
    glob["squares"] = {}
    glob["squares"][glob["pos"]] = False
    glob["unexplored"] = [glob["pos"]]

    reset_walls()

# Bug: If a wall disappears in unsearched squares_n it can get stuck
def maze(laps):

    for lap in range(laps):
        reset_grid()

        # Optimizing 10 teleports (random seed so will naturally vary tho)
        # 2216439                   Start
        # 869516    155% faster     Pre-generate outside walls
        # 441558    97% faster      Pathfind to closest unexplored
        # 290644    52% faster      Disabled grid reset after every teleport which was forgotten when I was debugging edge case
        # 238163    22% faster      Disabled unnecessary check for if current pos was unexplored, it will never be
        # 234431

        glob["teleports"] = 10  # Max is 299
        # glob["teleports"] = 299  # Max is 299
        glob["teleport_i"] = 0
        glob["treasure_pos"] = None
        glob["start_ops"] = get_tick_count()

        start_maze()
        if check_treasure():
            continue

        while True:
            # We can pathfind directly to treasure
            if glob["treasure_pos"] and get_square(glob["treasure_pos"]) != None:
                # quick_print("go to treasure")
                pathfind(glob["treasure_pos"])
                if fertilize_or_harvest_treasure():
                    break

            # Keep exploring
            else:
                # quick_print("explore")
                moved = explore_one_square()
                if moved:
                    if check_treasure():
                        break
                else:
                    pathfind(glob["unexplored"][-1])







