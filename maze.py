

from builtz.built import *




def maze(laps):
    for lap in range(laps):
        clear()
        plant(Entities.Bush)
        while get_entity_type() == Entities.Bush:
            use_item(Items.Fertilizer)

maze(1)

