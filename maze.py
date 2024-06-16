

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



# Bug: If a wall disappears in unsearched squares it can get stuck
def maze(laps):
    for lap in range(laps):
        pos = get_pos()

        grid = blank_grid()

        start_maze()
        back_track = False
        treasure_pos = None
        treasure_grid_pos = None

        # Max is 299, but I think there's an edge case where it teleports to same square twice and will be undetectable
        teleports = 2
        teleport_i = 0

        while True:
            do_measure = True
            while get_entity_type() == Entities.Treasure:
                if teleport_i == teleports:
                    harvest()
                    break

                if do_measure:
                    x, y = measure()
                    treasure_pos = [x, y]
                    treasure_grid_pos = grid[x][y]
                    if treasure_pos != pos:
                        teleport_i += 1
                        print(teleport_i)
                        do_measure = False

                        # set_execution_speed(0.5)

                use_item(Items.Fertilizer)

            if teleport_i == teleports:
                break

            if treasure_pos and treasure_grid_pos and False:
                print(treasure_pos)
                print(treasure_grid_pos)

            else:
                # Move one step

                do_next_square = False

                for dir_i in range(2):
                    directions = direction_indexes[dir_i]
                    for dir_ in directions:
                        grid_pos = grid[pos[0]][pos[1]]

                        # Already tried going through here, see if we should skip
                        if dir_ in grid_pos:
                            wall, wall_i = grid_pos[dir_]

                            # Always skip wall
                            if wall == WALL:
                                continue

                            # If info is from this iteration
                            if wall_i == teleport_i:
                                # Skip if open unless back tracking
                                if wall == OPEN and not back_track:
                                    continue

                                # Skip invisible wall (From back tracking)
                                if wall == WALL_INVIS:
                                    continue

                        result = move(dir_)
                        if result:
                            grid_pos[dir_] = [OPEN, teleport_i]
                        else:
                            grid_pos[dir_] = [WALL, teleport_i]

                        # If moved
                        if result:
                            update_pos(pos, dir_)
                            grid_pos = grid[pos[0]][pos[1]]
                            if back_track:
                                # Close off behind
                                grid_pos[direction_opposite[dir_]] = [WALL_INVIS, teleport_i]
                            else:
                                # Mark open behind
                                grid_pos[direction_opposite[dir_]] = [OPEN, teleport_i]

                            back_track = False
                            do_next_square = True
                            break
                    if do_next_square:
                        break

                # Dead-end, back track and close it off
                if not do_next_square:
                    back_track = True



