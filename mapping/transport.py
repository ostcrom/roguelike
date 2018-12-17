class Transport():
## TODO: In hindsight, this class should be converted to a GameObject probably,
##here we duplicate having position coordinates and then if we want to extend
##to have color as well (we do), we might as well have been using a GameObject.
    def __init__(self, x, y, dx, dy, new_map_index=None):
        self.x = x
        self.y = y

        self.dx = dx
        self.dy = dy

        if not new_map_index is None:
            self.new_map_index = new_map_index
        else:
            self.new_map_index = 0
