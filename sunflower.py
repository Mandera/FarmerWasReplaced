
from Main import *
from helpers import *
from builtz.built import *



def store_petals(dict_, x, y, petals):
    if petals not in dict_:
        dict_[petals] = []
    dict_[petals].append((x, y))


def sunflowers(laps, setup=True):
    dict_ = {}

    buy_items(Items.Sunflower_Seed, squares * laps)

    if setup:
        for x in range(size):
            y = 0
            for y in range(size_min_1):
                till()
                plant(Entities.Sunflower)
                use_item(Items.Water_Tank)
                store_petals(dict_, x, y, measure())
                move(East)
            till()
            plant(Entities.Sunflower)
            use_item(Items.Water_Tank)
            store_petals(dict_, x, y, measure())
            move(North)

    most = None
    most_x = None
    most_y = None

    for i in range(laps):
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
