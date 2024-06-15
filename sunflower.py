
from Main import *
from helpers import *
from builtz.built import *



def store_petals(dict_, x, y, petals):
    if petals not in dict_:
        dict_[petals] = []
    dict_[petals].insert(0, (x, y))


def sunflowers(laps, setup=True):
    dict_ = {}
    buy_items(Items.Sunflower_Seed, squares * laps)

    for i in range(laps):
        clear()
        x = 0
        y = 0
        for i2 in range(size):
            for i3 in range(size_min_1):
                if y > 4:
                    use_item(Items.Water_Tank)
                harvest()
                till()
                plant(Entities.Sunflower)
                store_petals(dict_, x, y, measure())
                move(East)
                x = (x + 1) % size
            if y > 4:
                use_item(Items.Water_Tank)
            harvest()
            till()
            plant(Entities.Sunflower)
            store_petals(dict_, x, y, measure())
            move(North)
            y = (y + 1) % size

        while dict_:
            keys = list(dict_)
            max_petals = max(keys)
            for coords in dict_[max_petals]:
                goto(coords)
                while not can_harvest():
                    pass
                harvest()
            dict_.pop(max_petals)







