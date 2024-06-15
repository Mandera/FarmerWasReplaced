from builtz.built import harvest, till, plant, Entities, move, East


def do_tree(i, direction):
    if i:
        harvest()
    else:
        till()
    plant(Entities.Tree)
    # use_item(Items.Water_Tank)
    move(East)
    move(direction)
