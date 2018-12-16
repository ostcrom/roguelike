from mapping.space import Space
class GameMap:
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.build_instruction_set = []
        self.spaces = []
        self.transports = []


    def init_spaces(self):
        self.spaces = [[Space(True) for y in range(self.height)] for x in range(self.width)]
        self.add_room(1,1,5,5)
        self.add_tunnel_h(5,3,35)
        self.add_tunnel_v(40,3,20)
        self.add_room(30,23,15,10)
        self.add_tunnel_v(35,33,10)
        self.add_room(32,43,5,5)
        self.add_tunnel_h(37,45,25)
        self.add_room(62,23,10,25)
        self.add_tunnel_h(45,25,20)

        self.dig_map()
        self.load_transports()

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

    def dig(self, x, y):
        """
        Funtion to clear wall out of the mapself.
        x and y are int coord.
        """
        if x >= 0 and x <= self.width:
            if y >= 0 and y <= self.height:
                self.spaces[x][y].blocked = False
                self.spaces[x][y].block_sight = False

    def load_transports(self, transports):
        for transport in

    def add_build_instruction(self, pos_x, pos_y, scale_x, scale_y):
        """
        pos_x and pos_y are x,y coordinates on map for top left corner
        of the square to be dug out.
        scale_x and scale_y are scalars for width and height of square

        This function appends an array to a class instanced list which is used
        to carve out a map from a set of such arrays.
        """
        self.build_instruction_set.append([pos_x, pos_y, scale_x, scale_y])

    def dig_map(self):
        """
        This function processes the list of arrays which represents the rooms to
        be dug out of the map, which by default has all squares have "is_blocked"
        set to True.
        This iterates through the list and calls the next function which "digs"
        the rooms out.
        """
        for struct in self.build_instruction_set:
            self.dig_square(struct[0],struct[1],struct[2],struct[3])

    def dig_square(self, pos_x, pos_y, scale_x, scale_y):
        """
        This function digs the squares the parameters correspond to
        add_build_instruction()
        """
        for x in range(pos_x,  pos_x + scale_x):
            for y in range(pos_y, pos_y + scale_y):
                self.dig(x,y)

    """
    The functions below further abstract the process of adding  build instruc-
    tions so it possible to 'build' a map by specifying a series of rooms and
    tunnels.
    """
    def add_room(self,pos_x, pos_y, scale_x, scale_y):
        self.add_build_instruction(pos_x, pos_y, scale_x, scale_y)

    def add_tunnel_v(self,pos_x,pos_y,scale_y):
        self.add_build_instruction(pos_x,pos_y,1,scale_y)

    def add_tunnel_h(self,pos_x,pos_y,scale_x):
        self.add_build_instruction(pos_x,pos_y,scale_x,1)
