
from builtz.built import *
# from carrot import carrots
# from hay import hay
# from pumpkin import pumpkins
# from tree import tree
from helpers import *


# Wait with this until we have lists and dictionaries


size = get_world_size()
size_min_1 = size - 1
squares = size * size
diagonals = 4
uneven = size % 2
half_size = size / 2

direction_indexes = [[East, West], [North, South]]



goto((2, 1))


# while True:
#     clear()
#
#     # tree(100)
#     pumpkins(100)
#
#     hay_num = num_items(Items.Hay)
#     wood_num = num_items(Items.Wood)
#     carrots_num = num_items(Items.Carrot)
#     pumpkins_num = num_items(Items.Pumpkin)
#
#     if hay_num < 1000000:
#         hay(100)
#     elif wood_num < 1000000:
#         tree(100)
#     elif pumpkins_num < 1000000:
#         pumpkins(50)
#     else:
#         carrots(100)

