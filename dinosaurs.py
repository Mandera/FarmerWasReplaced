# Much room for improvement but this works
# Could do more in memory

from Main import *
from helpers import *
from builtz.built import *



def move_dino():
    dino_type = measure()
    if random() > 0.5:
        dir_a, dir_b = dino_dirs[dino_type]
    else:
        dir_b, dir_a = dino_dirs[dino_type]

    for dir_ in (dir_a, dir_b):
        other_dino_type = measure(dir_)
        if dino_type != other_dino_type:
            swap(dir_)
            break


def dinosaur(laps):
    buy_items(Items.Egg, squares_n * laps)

    # Till and plant
    for i2 in range(size):
        for i3 in range(size_min_1):
            till()
            use_item(Items.Egg)
            move(East)
        till()
        use_item(Items.Egg)
        move(North)

    for lap_i in range(laps):
        # Move dinos
        for move_lap in range(10):
            for i in range(size):
                for i2 in range(size):
                    move_dino()
                    move(East)
                move_dino()
                move(North)

        goto((0, 0))
        harvest()
        move(South)
        harvest()
        move(West)
        harvest()
        move(North)
        harvest()

        if lap_i == laps - 1:
            break

        # Only replant, might yield warnings for left behind dinos but that's fine
        for i2 in range(size):
            for i3 in range(size_min_1):
                use_item(Items.Egg)
                move(East)
            use_item(Items.Egg)
            move(North)

