from Main import size, size_min_1
from builtz.built import till, harvest, can_harvest, plant, Entities, use_item, Items, move, North, East


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
