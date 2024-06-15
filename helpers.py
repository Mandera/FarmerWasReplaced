from builtz.built import num_items, trade


def buy_items(item, target):
    current = num_items(item)
    if current < target:
        trade(item, target - current)
