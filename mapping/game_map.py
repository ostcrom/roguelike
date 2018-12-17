from mapping.space import Space
from mapping.map_loader import MapLoader
from mapping.transport import Transport

class GameMap:
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.build_instruction_set = []
        self.spaces = []
        self.transports = []
        self.map_loader = MapLoader(self.width, self.height)

    def switch_map(self, map_index=0):
        self.spaces = self.map_loader.load_map(map_index)

    def is_blocked(self, x, y):
        if self.spaces[x][y].blocked:
            return True

        return False

    def is_transport(self, x, y):
        if self.spaces[x][y].transport:
            return True

        return False

    def update_blocked(self, entities):
        for entity in entities:
            if entity.blocks:
                self.spaces[entity.x][entity.y].blocked = True

    def unblock(self, x, y):
        self.spaces[x][y].blocked = False
