from bearlibterminal import terminal
from mapping.game_map import GameMap
from gameplay.dialog_tree import DialogTree
from message_log import MessageLog
from game_object import GameObject
from render_functions import draw_all, draw_map
from input_handler import handle_keys
from utils import test_dict, map_npc_db, lorem, get_truth
from gameplay.npc import NPC
from gameplay.inventory import InventoryItem

game_title = "StrangeHack"
screen_width = 120
screen_height = 40
map_width=65
map_height = 40
dialog_width = 50
dialog_height = 35
dialog_pos_x = 68
dialog_pos_y = 1
##Todo: This is starting to turn into spaghetti code. Probably need to refactor
##soon.
def updateui():
        ##Switch to layer 4 to update UI

        terminal.layer(3)
        terminal.clear_area(dialog_pos_x,dialog_pos_y,dialog_width,dialog_height)
        terminal.printf(dialog_pos_x,dialog_pos_y,ml.get_scroll_back())
        terminal.refresh()

def selection_to_int(selection):
    ##This seems like an incredibly hacky way to do this but I do not see this
    ##functionality built into the bearlibterm for some reason.. :(

    ##TODO, ENUMERATE through "terminal" and get all properties whose key starts
    ##"TK_" Then lop off the end and return it as a char.
    if selection == terminal.TK_1:
        return 1
    elif selection == terminal.TK_2:
        return 2
    elif selection == terminal.TK_3:
        return 3
    elif selection == terminal.TK_4:
        return 4
    elif selection == terminal.TK_5:
        return 5
    elif selection == terminal.TK_6:
        return 6
    elif selection == terminal.TK_7:
        return 7
    elif selection == terminal.TK_8:
        return 8
    elif selection == terminal.TK_9:
        return 9
    else:
        return None


def dialog_condition_check(condition_code_string, char1, char2):
    code_string_stack = condition_code_string.split(" ")
    ##OK, so here's the deal.
    ##conditions will be specified in dialog tree as a stringself.
    ##the string will have 3 positions to start, separated by spaces,
    ##except the third position in some cases but we'll get to that.
    ##Returns a dang bool holmes!

    ##First position is the trigger variable, which has to be a property
    ##on the player object or a keyword like item

    try:

        trigger_var_str = code_string_stack.pop(0)
        trigger_var_str = trigger_var_str.lower()
        #second pos is the comparison operator
        operator_str = code_string_stack.pop(0)
        ##the third pos is whatever bits are remaining (to be split again later maybe)
        ##join it
        condition_str = str.join(" ", code_string_stack)
        print(trigger_var_str)
        print(operator_str)
        print(condition_str)
    except:
        print("Couldn't  parse condition string.")
        return False

        ##Special case to check inventory items...
    if trigger_var_str == 'item':
        inventory = getattr(player, 'inventory', None)
        for item in inventory:
            print(item)
        if condition_str in inventory:
            return True
        else:
            return False
        ##Need to add extra conditions to check item quantity.

    try:
        trigger = getattr(player, trigger_var_str)
    except:
        print("Couldn't get player attribute " + trigger_var_str)
        return False
    print("Returning THE truth!")
    return get_truth(trigger, operator_str, condition_str)

def npc_dialog(npc, player, dialog_name):
    dialog_tree = DialogTree(npc.dialog_dict)
    text = dialog_tree.get_say(dialog_name)
    conditions = dialog_tree.get_conditions(dialog_name)
    responses = dialog_tree.get_responses(dialog_name)
    target = dialog_tree.get_target_dialog(dialog_name)


    if not conditions is None:
        exit = False
        for condition in conditions:
            exit = not dialog_condition_check(condition['condition_string'], player, npc)
        if exit:
            return False

    ml.log_message(text)
    if not responses is None:
        response_count = 1
        for response in responses:
            ml.log_message(str(response_count) + ".) " + response['say'] + " (" + response['target_dialog'] + ")")
            response_count += 1
        updateui()

        selected_response = None

        while selected_response is None:
            if terminal.has_input():
                selection = terminal.read()
                if selection == terminal.TK_ESCAPE:
                    selected_response = 99
                else:
                    selected_response = selection_to_int(selection)
                if not selected_response is None and selected_response >= 0 and selected_response < response_count:
                    ##Subtract one from selection because count starts at 1 not 0
                    target = responses[selected_response - 1]["target_dialog"]
                else:
                    ml.log_message("Select a response from 1 to " + str(response_count - 1 ))
            else:
                pass
            updateui()

    if dialog_tree.dialog_exists(target):
        npc_dialog(dialog_tree, player,  target)

def load_map(terminal, player, objects, map, new_map_index=0, dx=0, dy=0):
    map.switch_map(new_map_index)
    draw_map(terminal, map)
    game_map.unblock(player.x, player.y)
    player.move(dx , dy )
    objects.clear()
    objects.append(player)

    if map.map_name in map_npc_db:
        load_objects = map_npc_db[map.map_name]

        for key in load_objects.keys():
            objects.append(init_object(load_objects[key], key))

def add_to_inventory(inventory, item_to_add):
    item_in_inventory = inventory.get(item_to_add.name, None)

    if item_in_inventory is None:

        inventory[item_to_add.name] = item_to_add
    else:
        item_in_inventory.quantity += item_to_add.quantity



def init_object(o, name):
    if not 'x' in o:
        o['x'] = 0
    if not 'y' in o:
        o['y'] = 0
    if not 'char' in o:
        o['char'] = '@'
    if not 'color' in o:
        o['color'] = 'black'

    if not 'type' in o:
        return GameObject(o['x'], o['y'], o['char'], o['color'], name)
    elif o.get('type') == 'npc':
        if 'dialog' in o:
            dialog = o['dialog']
        else:
            dialog = 'default'
        return NPC(o['x'], o['y'], o['char'], o['color'], name, dialog)

##TODO: abstract, automate init
terminal.open()
terminal.printf(1, 1, 'Hello, world!')
terminal.refresh()
terminal.set("window: size="+str(screen_width)+"x"+str(screen_height)+";")

run = True
ml = MessageLog(dialog_width, dialog_height)
test_count = 0

game_objects = []
dialog_entities = []


player = GameObject(3, 3, '@', 'red', "Hero", True)
player.inventory = {}

##Keep track of which direction player is pointing, start up.
player.last_dx = 0
player.last_dy = -1
game_objects.append(player)

add_to_inventory(player.inventory, InventoryItem("Goblet"))


game_map = GameMap(map_width,map_height)
load_map(terminal, player, game_objects, game_map)
draw_map(terminal, game_map)
draw_all(terminal, game_objects, map_width, map_height)
terminal.refresh()
while run:
    action = None

    if terminal.has_input():
        action = terminal.read()
        ##1202 AM TODO:
        ###implement map system in blt engine✅
        ###implement NPC and fold in dialog system✅
        ##by adding a 'dialog' property to NPC object.
        ###implement item class and item description

        ##0118 # TODO:
        ##implement conditionals✅ 0119

        if action == terminal.TK_CLOSE:
            run = False
            ##BS test functions for the moment.
            ### TODO: remove da bs
        elif action == terminal.TK_A:
            get_object = game_map.get_game_object(player.x + player.last_dx, player.y + player.last_dy, game_objects)
            print(str(player.x + player.last_dx) +" "+ str(player.y + player.last_dy))

            if not get_object is None:
                print(str(get_object))
                if isinstance(get_object, NPC):
                    if not get_object.dialog_dict is None:
                        dialog_tree = DialogTree(get_object.dialog_dict)
                        npc_dialog(get_object, player, "main")


        elif action == terminal.TK_S:
            ml.log_message(lorem + " " + str(test_count))
        elif action == terminal.TK_M:
            dialog_tree = DialogTree()
            npc_dialog(dialog_tree, 'main')
        control = handle_keys(action)
        move = control.get('move')

        if move:
            dx,dy = move
            new_x = player.x + dx
            new_y = player.y + dy
            if game_map.is_transport(new_x, new_y):
                transport = game_map.spaces[new_x][new_y].transport
                load_map(terminal, player, game_objects, game_map,
                        transport.new_map_index, dx + transport.dx, dy + transport.dy)
            elif not game_map.is_blocked(new_x,new_y):
                game_map.unblock(player.x, player.y)
                player.move(dx,dy)

            player.last_dx = dx
            player.last_dy = dy
        test_count += 1

        draw_all(terminal, game_objects, map_width, map_height)
        updateui()

terminal.close()
##layers:
##background 0
##terrain 1
##characters 2
##ui 3
