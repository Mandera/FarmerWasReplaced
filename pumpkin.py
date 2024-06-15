from Main import squares, size, size_min_1
from helpers import buy_items
from builtz.built import get_entity_type, plant, move, Items, till, Entities, East, North, harvest


def pumpkin_harvest(seed, direction):
    planted = False
    if get_entity_type() == None:
        plant(seed)
        # use_item(Items.Water_Tank)
        planted = True
    move(direction)
    return planted


def pumpkins(laps, setup=True):
    buy_items(Items.Pumpkin_Seed, squares * laps)

    if setup:
        for x in range(size):
            for y in range(size_min_1):
                till()
                plant(Entities.Pumpkin)
                # use_item(Items.Water_Tank)
                move(East)
            till()
            plant(Entities.Pumpkin)
            # use_item(Items.Water_Tank)
            move(North)

    for i in range(laps):
        good = True
        for x in range(size):
            for i in range(size_min_1):
                if pumpkin_harvest(Entities.Pumpkin, East):
                    good = False
            if pumpkin_harvest(Entities.Pumpkin, North):
                good = False
        if good:
            harvest()
