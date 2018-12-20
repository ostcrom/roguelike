import libtcodpy as libtcod
import textwrap
from gameplay.dialog_tree import DialogTree
from ui import PromptHelper

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
        self.height = height
        self.width = width
        self.prompt_helper = PromptHelper(self.dialog_con, self.height, self.width, target_pos_x, target_pos_y, target_con)

        ##Set text line width to our prompt width minus a 10% margin.
        self.wrapper = textwrap.TextWrapper(width - width / 10 )


    def say_line(self, line_to_say):


        message = ''
        lines = self.wrapper.wrap(line_to_say)

        ##textwrapper returns an array of lines, None if empty.
        if lines is None:
            return
        ##Concatenate an array into a single string with line breaks.
        for line in lines:
            message += line + "\r\n"

        self.prompt_helper.set_text(message)
        self.prompt_helper.update()

    def unload(self):
        self.dialog_con.consoloe_delete()

    def get_reply(self, num_responses, tries):
        prompt_text = ''
        if tries == 1:
            prompt_text += "Select reply:\r\n"
        elif tries <= 3:
            prompt_text += "Please select a response: 1 - " + str(num_responses)+ "\r\n"
        else:
            return 0
        self.prompt_helper.set_text(prompt_text, True)
        selection = self.GetChoice()
        print(selection)

        if isinstance(selection,int) and not selection < 1 and not selection > num_responses:
            ##Numbers displayed for player use human counting. Subtract one so
            ##we get the appropriate array index.
            return selection - 1;
        else:
            return self.get_reply(num_responses, tries + 1)
    def GetChoice(self):
        command = ''
        key = libtcod.console_wait_for_keypress(True)
        while key.vk != libtcod.KEY_ENTER:
            letter = chr(key.c)
            x = len(command)
            libtcod.console_set_char(0, x,  0, letter)  #print new character at appropriate position on screen
            command = command + letter  #add to the string

            key = libtcod.console_wait_for_keypress(True)
        return command
