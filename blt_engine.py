from bearlibterminal import terminal
from mapping.game_map import GameMap
from gameplay.dialog_tree import DialogTree
from message_log import MessageLog

def updateui():
        ##Switch to layer 4 to update UI
        terminal.layer(4)
        terminal.clear_area(0,0,200,200)
        terminal.print(40,0,ml.get_scroll_back())
        terminal.refresh()

def selection_to_int(selection):
    ##This seems like an incredibly hacky way to do this but I do not see this
    ##functionality built into the bearlibterm for some reason.. :(

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

def npc_dialog(dialog_tree, dialog_name):
    text = dialog_tree.get_say(dialog_name)
    responses = dialog_tree.get_responses(dialog_name)
    target = dialog_tree.get_target_dialog(dialog_name)
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
                    print(target)
                else:
                    ml.log_message("Select a response from 1 to " + str(response_count -1 ))
            else:
                pass
            updateui()

    if dialog_tree.dialog_exists(target):
        npc_dialog(dialog_tree, target)

terminal.open()
terminal.printf(1, 1, 'Hello, world!')
terminal.refresh()

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

run = True
ml = MessageLog(35, 25)
test_count = 0

while run:
    action = None
    if terminal.has_input():
        action = terminal.read()

        if action == terminal.TK_CLOSE:
            run = False
        elif action == terminal.TK_A:
            ml.log_message("You pressed key! Lorem ipsum dolor sit amet, consectetur adipiscing el" + str(test_count))
            print(ml.get_scroll_back())

        elif action == terminal.TK_S:
            ml.log_message(lorem + " " + str(test_count))
        elif action == terminal.TK_M:
            dialog_tree = DialogTree()
            npc_dialog(dialog_tree, 'main')

        test_count += 1
        updateui()




terminal.close()
##layers:
##background
##terrain
##characters
##ui