class Transport():

    def __init__(self, x, y, dx, dy, new_map_index=None):
        self.x = x
        self.y = y

        self.dx = dx
        self.dy = dy

        if not new_map_index is None:
            self.new_map_index = new_map_index
        else:
            self.new_map_index = 0
