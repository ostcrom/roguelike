from bearlibterminal import terminal

FLOOR_LAYER = 0
MAP_LAYER = 1
ENTITY_LAYER = 2
UI_LAYER = 3
BLOCK = "█"

def draw_entity(terminal, entity):
    terminal.layer(ENTITY_LAYER)
    terminal.color(entity.color)
    terminal.put(entity.x, entity.y, entity.char)

def draw_map(terminal, game_map):
    terminal.layer(MAP_LAYER)
    clear_layer(terminal,MAP_LAYER,game_map.width, game_map.height)
    for y in range(game_map.height):
        for x in range(game_map.width):
            wall = game_map.spaces[x][y].block_sight
            transport = game_map.is_transport(x,y)

            if wall and not transport:
                terminal.color('blue')
                terminal.put(x,y,BLOCK)
                ##libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
            elif transport:
                terminal.color('green')
                terminal.put(x,y,BLOCK)
                ##libtcod.console_set_char_background(con, x, y, colors.get('transport_green'), libtcod.BKGND_SET)
            else:
                terminal.color('white')
                terminal.put(x,y,BLOCK)
                ##libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)


def draw_all(terminal, entities, w, h):

    clear_layer(terminal, ENTITY_LAYER, w, h)
    for entity in entities:
        draw_entity(terminal, entity)


def clear_layer(terminal, layer, w, h):
    terminal.layer(layer)
    terminal.clear_area(0,0,w,h)

def ui_print(terminal, x, y, h, w, text_string):

    terminal.layer(UI_LAYER)
    terminal.clear_area(dialog_pos_x,dialog_pos_y,dialog_width,dialog_height)
    terminal.printf(dialog_pos_x,dialog_pos_y,ml.get_scroll_back())
    terminal.refresh()
