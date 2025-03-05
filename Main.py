
from __builtins__ import *


size = get_world_size()
size_min_1 = size - 1
squares_n = size * size
diagonals = 4
uneven = size % 2
half_size = size / 2

all_directions = [North, East, South, West]  # No particular order
last_dir = all_directions[-1]
direction_indexes = [[East, West], [North, South]]
direction_numbers = {East: [0, 1], West: [0, -1], North: [1, 1], South: [1, -1]}
direction_opposite = {North: South, South: North, East: West, West: East}
direction_prefix = {North: ("h", ), South: ("h", ), East: ("v", ), West: ("v", )}
direction_wall_offset = {North: [1, 1], East: [0, 1]}
num_to_str = {-1: "-1", 0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10"}
direction_explore_reversed = {None: (North, East, South, West), North: (East, South, West), East: (South, West, North), South: (West, North, East), West: (North, East, South)}
direction_explore = {None: (North, East, South, West), North: (East, North, West), East: (South, East, North), South: (West, South, East), West: (North, West, South)}

OPEN = "open"
OUTSIDE_WALL = "OUTSIDE_WALL"

TELEPORTS_UNTIL_RECHECK_WALL = 3



dino_dirs = (
    (North, West),
    (North, East),
    (South, West),
    (South, East),
)


glob = {}

# clear()
# cactus(100)


unlocks = [
    Unlocks.Grass,          # 1     Grass

    Unlocks.Speed,          # 1     Grass
    Unlocks.Plant,          # 1     Grass
    Unlocks.Carrots,        # 2     Wood
    Unlocks.Trees,          # 2     Wood, Carrots
    Unlocks.Sunflowers,     #       Carrots
    Unlocks.Cactus,         #       Gold
    Unlocks.Dinosaurs,      #       Cactus

    Unlocks.Expand,         # 1     Grass (And Unlocks.Speed)
    Unlocks.Pumpkins,       #       Wood, Carrots
    Unlocks.Fertilizer,     #       Pumpkins
    Unlocks.Mazes,          #       Carrots, Pumpkins

    Unlocks.Polyculture,    #       Grass, Wood, Carrots (And Unlocks.Pumpkins - Not used yet tho)

    Unlocks.Leaderboard,    #       Bones (And Unlocks.Pumpkins)
]


# 1 - Grass
#   Balance Grass, Speed, Expand
#   End with Plant

# 2 - Bushes
#   Unlock Carrots
#   Get enough for Trees

# 3 - Carrots
#




# while True:
#     clear()
#
#     power_num = num_items(Items.Power)
#     hay_num = num_items(Items.Hay)
#     wood_num = num_items(Items.Wood)
#     carrots_num = num_items(Items.Carrot)
#     pumpkins_num = num_items(Items.Pumpkin)
#     gold_num = num_items(Items.Gold)
#     cactus_num = num_items(Items.Cactus)
#     bones_num = num_items(Items.Bones)
#
#     min_num = min(power_num, hay_num, wood_num, carrots_num, pumpkins_num, gold_num, cactus_num, bones_num)
#
#     if min_num == power_num:
#         sunflowers(10)
#     elif min_num == hay_num:
#         hay(10)
#     elif min_num == wood_num:
#         tree(10)
#     elif min_num == carrots_num:
#         carrots(10)
#     elif min_num == pumpkins_num:
#         pumpkins(10)
#     elif min_num == gold_num:
#         maze(10)
#     elif min_num == cactus_num:
#         cactus(10)
#     elif min_num == bones_num:
#         dinosaur(2)

