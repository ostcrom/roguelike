import libtcodpy as libtcod

def init_fov(game_map):
    fov_map = libtcod.map_new(game_map.width, game_map.height)

    for y in range(game_map.height):
        for x in range(game_map.width):
            libtcod.map_set_properties(fov_map,x,y)
