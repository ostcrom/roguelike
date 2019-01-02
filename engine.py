import libtcodpy as libtcod

from game_object import GameObject
from input_handler import handle_keys
from render_functions import clear_all, draw_all
from mapping.game_map import GameMap
from mapping.space import Space
from mapping.transport import Transport
from gameplay.dialog_prompt import DialogPrompt

game_title = "StrangeHack"
screen_width = 80
screen_height = 50
map_width=40
map_height = 40
dialog_width = 40
dialog_height = 20
dialog_pos_x = 40
dialog_pos_y = 21


fov_algorithm = 0
fov_light_walls = True

def main():

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)
    con = libtcod.console_new(screen_width, screen_height)
    dialog_prompt = DialogPrompt(dialog_pos_x, dialog_pos_y, "npc_dialog", dialog_width, dialog_height, con)

    game_map = GameMap(map_width, map_height)
    game_map.switch_map(0)

    fov_recomputer = True


    game_entities = []
    dialog_entities = []
    player = GameObject(3, 3, '@', libtcod.white, "Hero", True)
    npc = GameObject(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow, "Bad Guy", True)
    game_entities.append(player)
    game_entities.append(npc)
    key= libtcod.Key()
    mouse = libtcod.Mouse()
    libtcod.console_set_window_title(game_title+ " - " + game_map.map_name)
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        draw_all(con, game_entities, game_map, screen_width, screen_height)
        libtcod.console_flush()
        clear_all(con, game_entities)
        if key.c == ord('a'):
            dialog_prompt.npc_dialog('main')
        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')

        if move:
            dx, dy = move

            if not game_map.is_blocked(player.x + dx, player.y + dy) and not game_map.is_transport(player.x + dx, player.y + dy):
                game_map.unblock(player.x, player.y)
                player.move(dx,dy)
            elif game_map.is_transport(player.x + dx, player.y + dy):
                transport = game_map.spaces[player.x + dx][player.y + dy].transport
                game_map.switch_map(transport.new_map_index)
                libtcod.console_set_window_title( game_title + " - " + game_map.map_name)
                game_map.unblock(player.x, player.y)
                player.move(dx , dy )
                player.move(transport.dx, transport.dy)


        if key.vk == libtcod.KEY_ESCAPE:
            return True
        game_map.update_blocked(game_entities)

if __name__ == '__main__':
     main()
