class InventoryItem:
    def __init__(self, name, quantity = 1, stackable = False, item_attr = {}):
        self.name = name
        self.item_attr = item_attr
        self.stackable = stackable
        self.quantity = quantity
