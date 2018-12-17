from mapping.space import Space
from mapping.transport import Transport

class MapLoader:
    def __init__(self, w, h):
            """
            At some point this class should be oriented towards reading game
            resources from another format like json however for now we will
            use it to hard code our content.
            """
            self.width = w
            self.height = h

            self.list_of_instruction_sets = []
            self.list_of_transport_sets = []
            self.spaces = []
            self.build_instruction_set = []
            self.transports = []


            self.build_maps()



    def load_map(self, map_index):
        self.internal_game_map_reset()
        build_instruction_set = self.get_instruction_set(map_index)
        transport_set = self.get_transport_set(map_index)
        ###entit_set = self.entities

        self.dig_map(build_instruction_set)
        self.load_transports(transport_set)
        return self.spaces;


    def build_maps(self):
        """
        In the future we will load maps from something like json, for now we call
        hard coded methods to build our map.
        """
        self.level_0()
        self.level_1()

        print(self.list_of_instruction_sets)

    def get_instruction_set(self, map_index):
        return self.list_of_instruction_sets[map_index]

    def get_transport_set(self, map_index):
        return self.list_of_transport_sets[map_index]

    def internal_game_map_reset(self):
        self.spaces = [[Space(True) for y in range(self.height)] for x in range(self.width)]
        self.transports = []
        self.build_instruction_set = []

    def append_game_map_sets(self):
        self.list_of_instruction_sets.append(self.build_instruction_set.copy())
        self.list_of_transport_sets.append(self.transports.copy())
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
        for transport in transports:
            self.spaces[transport.x][transport.y].transport = transport

    def add_transport_instruction(self, x , y, dx, dy, new_map_index=None):
        self.transports.append(Transport(x, y, dx, dy, new_map_index))

    def add_build_instruction(self, pos_x, pos_y, scale_x, scale_y):
        """
        pos_x and pos_y are x,y coordinates on map for top left corner
        of the square to be dug out.
        scale_x and scale_y are scalars for width and height of square

        This function appends an array to a class instanced list which is used
        to carve out a map from a set of such arrays.
        """
        self.build_instruction_set.append([pos_x, pos_y, scale_x, scale_y])

    def dig_map(self, build_instruction_set):
        """
        This function processes the list of arrays which represents the rooms to
        be dug out of the map, which by default has all squares have "is_blocked"
        set to True.
        This iterates through the list and calls the next function which "digs"
        the rooms out.
        """
        for struct in build_instruction_set:
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
        """
        Aforementioned hardcoded build instructions for maps. Should provide build
        instructions and transports
        """

        def level_0(self):
            self.internal_game_map_reset()
            self.add_room(1,1,5,5)
            self.add_tunnel_h(5,3,10)

            self.append_game_map_sets()
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


    """
    Manually define our maps for now.
    """
    def level_0(self):
        self.internal_game_map_reset()

        self.add_room(1,1,5,5)
        self.add_tunnel_h(5,3,10)
        self.add_room(15,1,10,5)
        self.add_transport_instruction(22,1,0,1,1)

        self.append_game_map_sets()

    def level_1(self):
        self.internal_game_map_reset()
        self.add_transport_instruction(22,1,0,1,0)
        self.add_room(15,1,10,5)
        self.add_tunnel_v(20,6,10)
        self.add_room(15,16,10,10)


        self.append_game_map_sets()
