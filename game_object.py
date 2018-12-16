from mapping.game_map import GameMap

class GameObject:
    """
    A generic object to represent players, enemies, items, etcself.
    """

    def __init__(self, x, y, char, color, name, blocks=False):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks

    def move(self,dx,dy):
        self.x += dx
        self.y += dy