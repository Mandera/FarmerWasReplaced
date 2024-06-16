

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


def update_pos(pos, dir_):
    numbers = direction_numbers[dir_]
    pos[numbers[0]] = (pos[numbers[0]] + numbers[1]) % size


def maze(laps):
    for lap in range(laps):
        pos = get_pos()

        grid = blank_grid()

        start_maze()
        back_track = False

        while True:
            if get_entity_type() == Entities.Treasure:
                harvest()
                break

            do_next_square = False

            for dir_i in range(2):
                directions = direction_indexes[dir_i]
                for dir_ in directions:
                    grid_pos = grid[pos[0]][pos[1]]

                    # Already tried going through here
                    if dir_ in grid_pos:
                        # If open
                        if grid_pos[dir_]:
                            if not back_track:
                                continue
                        # Skip if closed
                        else:
                            continue

                    grid_pos[dir_] = move(dir_)

                    # Successfully moved through new
                    if grid_pos[dir_]:
                        update_pos(pos, dir_)
                        grid[pos[0]][pos[1]][direction_opposite[dir_]] = not back_track
                        back_track = False
                        do_next_square = True
                        break
                if do_next_square:
                    break

            # Dead-end, back track and close it off
            if not do_next_square:
                back_track = True



