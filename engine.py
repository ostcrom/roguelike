import libtcodpy as libtcod

from game_object import GameObject
from input_handler import handle_keys
from render_functions import clear_all, draw_all
from mapping.game_map import GameMap
from mapping.space import Space

screen_width = 80
screen_height = 50
map_width=100
map_height = 100


def main():

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)
    con = libtcod.console_new(screen_width, screen_height)

    game_map = GameMap(map_width, map_height)
    game_map.init_spaces()


    entities = []
    player = GameObject(int(screen_width/2), int(screen_height /2), '@', libtcod.white, "Hero", True)
    npc = GameObject(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow, "Bad Guy", True)
    entities.append(player)
    entities.append(npc)
    key= libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        draw_all(con, entities, game_map, screen_width, screen_height)
        libtcod.console_flush()
        clear_all(con, entities)
        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')

        if move:
            dx, dy = move

            if not game_map.is_blocked(player.x + dx, player.y + dy):
                game_map.unblock(player.x, player.y)
                player.move(dx,dy)
                if game_map.is_transport:
                    pass


        if key.vk == libtcod.KEY_ESCAPE:
            return True
        game_map.update_blocked(entities)

def load_game():
    print('hi')

if __name__ == '__main__':
     main()
