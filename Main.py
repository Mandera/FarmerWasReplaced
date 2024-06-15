
from builtins import *


def do_tree(i, direction):
    if i:
        harvest()
    else:
        till()
    plant(Entities.Tree)
    # use_item(Items.Water_Tank)
    move(East)
    move(direction)


def tree(laps):
    for i in range(laps):
        for x in range(size):
            for y in range(diagonals):
                do_tree(i, East)
            do_tree(i, North)
        while not can_harvest():
            pass


# Wait with this until we have lists and dictionaries
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



def buy_items(item, target):
    current = num_items(item)
    if current < target:
        trade(item, target - current)


def do_harvest(seed, direction):
    harvest()
    plant(seed)
    use_item(Items.Water_Tank)
    move(direction)

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
                do_harvest(Entities.Carrots, East)
            if x:
                do_harvest(Entities.Carrots, North)
            else:
                do_harvest(Entities.Sunflower, North)

        while not can_harvest():
            pass


def hay(laps, setup=True):
    till()

    for i in range(laps):
        for x in range(size):
            if x:
                harvest()
            else:
                while not can_harvest() and i:
                    pass
                harvest()
                plant(Entities.Sunflower)
                use_item(Items.Water_Tank)
            move(North)
            for y in range(size_min_1):
                harvest()
                move(East)


size = get_world_size()
size_min_1 = size - 1
squares = size * size
diagonals = 4
uneven = size % 2


while True:
    clear()

    # tree(100)
    pumpkins(100)

    hay_num = num_items(Items.Hay)
    wood_num = num_items(Items.Wood)
    carrots_num = num_items(Items.Carrot)
    pumpkins_num = num_items(Items.Pumpkin)
    
    if hay_num < 1000000:
        hay(100)
    elif wood_num < 1000000:
        tree(100)
    elif pumpkins_num < 1000000:
        pumpkins(50)
    else:
        carrots(100)

