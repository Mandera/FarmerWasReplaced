from Main import size, size_min_1, squares
from helpers import buy_items
from builtz.built import till, plant, Entities, use_item, Items, move, East, North, measure, print


def sunflowers(laps, setup=True):
    if setup:
        for x in range(size):
            for y in range(size_min_1):
                till()
                plant(Entities.Sunflower)
                use_item(Items.Water_Tank)
                move(East)
            till()
            plant(Entities.Sunflower)
            use_item(Items.Water_Tank)
            move(North)

    buy_items(Items.Sunflower_Seed, squares * laps)

    most = None
    most_x = None
    most_y = None

    for i in range(1):
        for x in range(size):
            for y in range(size_min_1):
                measurement = measure()
                if most == None or measurement > most:
                    most = measurement
                    most_x = x
                    most_y = y
                move(East)
            measurement = measure()
            if most == None or measurement > most:
                most = measurement
                most_x = x
                most_y = y
            move(North)
        print(most, most_x, most_y)
