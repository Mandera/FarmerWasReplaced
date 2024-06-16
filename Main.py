
from carrot import carrots
from hay import hay
from maze import maze
from pumpkin import pumpkins
from tree import tree
from helpers import *
from sunflower import sunflowers
from builtz.built import *



size = get_world_size()
size_min_1 = size - 1
squares = size * size
diagonals = 4
uneven = size % 2
half_size = size / 2

direction_indexes = [[East, West], [North, South]]
direction_numbers = {East: [0, 1], West: [0, -1], North: [1, 1], South: [1, -1]}
direction_opposite = {North: South, South: North, East: West, West: East}

maze(1)


while True:
    clear()

    power_num = num_items(Items.Power)
    hay_num = num_items(Items.Hay)
    wood_num = num_items(Items.Wood)
    carrots_num = num_items(Items.Carrot)
    pumpkins_num = num_items(Items.Pumpkin)

    # pumpkins_num = 0

    min_num = min(power_num, hay_num, wood_num, carrots_num, pumpkins_num)

    if min_num == power_num:
        sunflowers(10)
    elif min_num == hay_num:
        hay(10)
    elif min_num == wood_num:
        tree(10)
    elif min_num == carrots_num:
        carrots(10)
    elif min_num == pumpkins_num:
        pumpkins(10)

