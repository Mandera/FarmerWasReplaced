

from Main import *


def start_maze():
    plant(Entities.Bush)
    while get_entity_type() == Entities.Bush:
        use_item(Items.Fertilizer)


def blank_grid():
    grid = {}
    for x in range(size):
        grid[x] = {}
        for y in range(size):
            grid[x][y] = {}
    return grid

def get_grid_pos(grid, pos):
    if pos:
        x, y = pos
        return grid[x][y]

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
            glob["treasure_grid_pos"] = get_grid_pos(glob["grid"], glob["treasure_pos"])

            if glob["treasure_pos"] != glob["pos"]:
                glob["teleport_i"] += 1
                do_measure = False
                # set_execution_speed(0.5)
        use_item(Items.Fertilizer)

def tracked_move(dir_):
    result = move(dir_)
    if result:
        i, value = direction_numbers[dir_]
        glob["pos"][i] = (glob["pos"][i] + value) % size
        glob["grid_pos"] = get_grid_pos(glob["grid"], glob["pos"])
    return result

def try_move_dir(dir_):
    # Already tried going through here, see if we should skip
    if dir_ in glob["grid_pos"]:
        wall, wall_i = glob["grid_pos"][dir_]

        # Always skip wall
        if wall == WALL:
            return False

        # If wall info is from this iteration
        if wall_i == glob["teleport_i"]:
            # Skip if open unless back tracking
            if wall == OPEN and not glob["back_track"]:
                return False

            # Skip invisible wall (From back tracking)
            if wall == WALL_INVIS:
                return False

    prev_grid_pos = glob["grid_pos"]

    # Successfully moved
    if tracked_move(dir_):
        prev_grid_pos[dir_] = [OPEN, glob["teleport_i"]]
        if glob["back_track"]:
            # Close off behind temporarily
            glob["grid_pos"][direction_opposite[dir_]] = [WALL_INVIS, glob["teleport_i"]]
        else:
            # Mark open behind
            glob["grid_pos"][direction_opposite[dir_]] = [OPEN, glob["teleport_i"]]

        glob["back_track"] = False
        return True

    # There's a wall
    else:
        glob["grid_pos"][dir_] = [WALL, glob["teleport_i"]]

def make_move():
    for dir_i in range(2):
        directions = direction_indexes[dir_i]
        for dir_ in directions:
            if try_move_dir(dir_):
                return True
    # Dead-end, enable back track
    glob["back_track"] = True



# Bug: If a wall disappears in unsearched squares it can get stuck
def maze(laps):
    for lap in range(laps):
        glob["pos"] = get_pos()
        glob["grid"] = blank_grid()
        glob["grid_pos"] = get_grid_pos(glob["grid"], glob["pos"])
        glob["teleports"] = 2  # Max is 299, but I think there's an edge case where it teleports to same square twice and will be undetectable
        glob["teleport_i"] = 0
        glob["back_track"] = False
        glob["treasure_pos"] = None

        start_maze()

        while True:
            if check_treasure():
                # Chest was harvested
                break

            if not glob["treasure_pos"]:
                quick_print("treasure not found")
                make_move()

            elif not glob["treasure_grid_pos"]:
                quick_print("treasure found but square not discovered")
                make_move()

            else:
                quick_print("treasure found and discovered")






