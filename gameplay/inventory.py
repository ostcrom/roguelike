class InventoryItem:
    def __init__(self, name, item_attr = {}, stackable = False, quantity = 1):
        self.name = name
        self.item_attr = item_attr
        self.stackable = stackable
        self.quantity = quantity
