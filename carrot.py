from Main import size, size_min_1, squares
from helpers import buy_items
from builtz.built import till, move, East, North, Items, Entities, can_harvest, harvest, plant, use_item


def carrots(laps, setup=True):
    if setup:
        for x in range(size):
            for y in range(size_min_1):
                till()
                move(East)
            till()
            move(North)

    buy_items(Items.Carrot_Seed, squares * laps)
    for i in range(laps):
        for x in range(size):
            for y in range(size_min_1):
                carrot_harvest(Entities.Carrots, East)
            if x:
                carrot_harvest(Entities.Carrots, North)
            else:
                carrot_harvest(Entities.Sunflower, North)

        while not can_harvest():
            pass


def carrot_harvest(seed, direction):
    harvest()
    plant(seed)
    use_item(Items.Water_Tank)
    move(direction)