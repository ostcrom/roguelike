
class GameObject:
    """
    A generic object to represent players, enemies, items, etcself.
    """

    def __init__(self, x, y, char, color, name, blocks=False, fov_radius=10):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks
        self.fov_radius = fov_radius
        self.enabled = True

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def enable(self):
        if not self.enable is True:
            self.enable = True

    def disable(self):
        if not self.enable is False:
            self.enable = False

    ##Derivative objects can override update.
    def update():
        pass
