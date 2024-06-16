

from Main import *


def start_maze():
    clear()
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
        pos = [0, 0]
        stack = [pos]

        grid = blank_grid()

        start_maze()

        while True:
            for dir_i in range(2):
                directions = direction_indexes[dir_i]
                result = None
                for dir_ in directions:


                    result = move(dir_)
                    grid[pos[0]][pos[1]][dir_] = result
                    if result:
                        update_pos(pos, dir_)
                        grid[pos[0]][pos[1]][direction_opposite[dir_]] = True
                        break
                if result:
                    break



