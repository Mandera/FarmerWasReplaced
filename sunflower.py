# Working but had to disable watering, doesn't take water inventory into account



from Main import *
from helpers import *
from __builtins__ import *



def store_petals(dict_, x, y, petals):
    if petals not in dict_:
        dict_[petals] = []
    dict_[petals].append((x, y))


def sunflower(laps, setup=True):
    dict_ = {}
    replants = 1000
    water_limit = 0.75
    plants = (squares_n + replants) * laps

    for i in range(laps):
        x = 0
        y = 0
        for i2 in range(size):
            for i3 in range(size_min_1):
                if not i:
                    till()
                plant(Entities.Sunflower)
                # while get_water() < water_limit:
                #     use_item(Items.Water)
                store_petals(dict_, x, y, measure())
                move(East)
                x = (x + 1) % size
            if not i:
                till()
            plant(Entities.Sunflower)
            # while get_water() < water_limit:
            #     use_item(Items.Water)
            store_petals(dict_, x, y, measure())
            move(North)
            y = (y + 1) % size

        n = 0
        while dict_:
            keys = list(dict_)
            max_petals = max(keys)
            list_ = dict_[max_petals]
            while list_:
                n += 1
                coords = list_.pop(0)
                x, y = coords
                goto(coords)
                if not can_harvest():
                    use_item(Items.Fertilizer)
                    # for i2 in range(4):
                    #     use_item(Items.Water)
                harvest()

                if n < replants:
                    plant(Entities.Sunflower)
                    petals = measure()
                    store_petals(dict_, x, y, petals)
                    if petals > max_petals:
                        break

            if not list_:
                dict_.pop(max_petals)
        goto((0, 0))




