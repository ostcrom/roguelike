import libtcodpy as libtcod
import textwrap
from gameplay.dialog_tree import DialogTree

test_dict = {"main":{
    "say": "Hi there this top level dialog!",
    "response":[{"say":"Thank you! Whats next?", "target_dialog":"answer_happy"},
            {"say":"Get that corn outta my face!", "target_dialog":"answer_indignant"},
            {"say":"Can I have the dialog tutorial?","target_dialog":"example_dialog"}],
    },
    "answer_happy":{
        "say":"Well, how about I invite you to my finished basement apartment, located conveniently under my parents house. I have imitation crab meat to share!",
        "emote":"You back away slowly.",
        "target_dialog":"exit"
    },
    "answer_indignant":{
        "say":"If the elastic hadn't broken in my stretchy pants, I would kick your ass.",
        "target_dialog":"exit"
    },

    "example_dialog":{
        "say":"This example dialog will provide a dialog object with all possible keys and demonstrate the order dialog objects are processed in, which is respective to the order found within this code. IE: The 'say' key is processed first, followed by the response key.",
        "response":[{"say":"I think that makes sense.", "target_dialog":"answer_happy"},
                    {"say":"I like turtles and nested json objects", "target_dialog":"answer_indignant"}]
    }
}

class DialogPrompt(DialogTree):
    def __init__(self, target_con, width, height, target_pos_x, target_pos_y):
        super().__init__(test_dict)
        self.dialog_con = libtcod.console_new(width,height)
        self.target_con = target_con
        self.target_pos_x = target_pos_x
        self.target_pos_y = target_pos_y
        self.wrapper = textwrap.TextWrapper(width - width / 10 )

    def say_line(self, line_to_say):
        message = ''
        lines = self.wrapper.wrap(line_to_say)

        for line in lines:
            message += line + "\r\n"

        libtcod.console_print_ex(self.dialog_con, 1, 1, libtcod.BKGND_NONE, libtcod.LEFT, message )
        libtcod.console_blit(self.dialog_con,0,0,0,0,self.target_con, self.target_pos_x, self.target_pos_y)
        libtcod.console_flush()

    def unload(self):
        self.dialog_con.consoloe_delete()

    def get_reply(self, num_responses, tries):
        if tries == 1:
            print ("Select reply:")
        elif tries <= 3:
            print ("Please select a response: 1 - " + str(num_responses))
        else:
            return 0
        selection = self.GetInput()
        print(selection)

        if isinstance(selection,int) and not selection < 1 and not selection > num_responses:
            ##Numbers displayed for player use human counting. Subtract one so
            ##we get the appropriate array index.
            return selection - 1;
        else:
            return self.get_reply(num_responses, tries + 1)
    def GetInput(self):
        command = ''
        key = libtcod.console_wait_for_keypress(True)
        while key.vk != libtcod.KEY_ENTER:
            letter = chr(key.c)
            x = len(command)
            libtcod.console_set_char(0, x,  0, letter)  #print new character at appropriate position on screen
            command = command + letter  #add to the string

            key = libtcod.console_wait_for_keypress(True)
        return command
