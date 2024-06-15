

from built import *


# trade(Items.Fertilizer, 1000)

clear()

plant(Entities.Bush)
use_item(Items.Water_Tank)
use_item(Items.Water_Tank)
use_item(Items.Water_Tank)


while not can_harvest():
    pass

while get_entity_type() == Entities.Bush:
    use_item(Items.Fertilizer)



