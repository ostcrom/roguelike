import libtcodpy as libtcod
import textwrap
from gameplay.dialog_tree import DialogTree
from game_object import GameObject


test_dict = {"main":{
    "say": "Hi there this is an example of top level dialog!",
    "response":[{"say":"Thank you! Whats next?", "target_dialog":"answer_happy"},
            {"say":"Get that corn outta my face!", "target_dialog":"answer_indignant"},
            {"say":"Can I have the dialog tutorial?","target_dialog":"example_dialog"}],
    "target_dialog":"example_dialog"
    },
    "answer_happy":{
        "say":"Well, how about I invite you to my finished basement apartment, located conveniently under my parents house. I have imitation crab meat to share!",
        "emote":"You back away slowly.",
        "target_dialog":"exit"
    },
    "answer_indignant":{
        "say":"If the elastic hadn't broken in my stretchy pants, I would kick your ass.",
        "target_dialog":"answer_happy"
    },

    "example_dialog":{
        "say":"This example dialog will provide a dialog object with all possible keys and demonstrate the order dialog objects are processed in, which is respective to the order found within this code. IE: The 'say' key is processed first, followed by the response key.",
        "response":[{"say":"I think that makes sense.", "target_dialog":"answer_happy"},
                    {"say":"I like turtles and nested json objects", "target_dialog":"answer_indignant"}],
        "target_dialog":"answer_happy"
    }
}

class DialogPrompt(GameObject):
    def __init__(self, x, y, name, width, height, target_con, dialog_dict=test_dict):
        super().__init__(x, y, ' ', 'todo-color', name)
        self.dialog_con = libtcod.console_new(width,height)

        self.target_con = target_con
        self.height = height
        self.width = width
        self.dialog_tree = DialogTree(dialog_dict, width, height)
        self.prompt_text = ''
        self.wait_for_reply = False
        self.exit = True

        self.wrapper = textwrap.TextWrapper(width - width / 10 )

    def npc_dialog(self, dialog_name='main', clear=True, target_dialog=None):

        if target_dialog == "exit":
            return
        ##Clear if clear==true
        self.clear_prompt_text(clear)

        target_dialog = self.dialog_say(dialog_name, False, target_dialog)
        self.blank_line(2)
        target_dialog = self.dialog_reply(dialog_name, False, target_dialog)
        self.blank_line(2)

        if not target_dialog is None:

            self.npc_dialog(target_dialog, False, target_dialog)

    def dialog_say(self, dialog_name, clear=False, target_dialog=None):
        ##clear prompt if True
        ##TODO:This check may not be necessary everywhere..
        self.clear_prompt_text(clear)
        say = self.dialog_tree.get_say(dialog_name)
        if not say is None:
            self.append_prompt_text(say)
            self.update()
        self.update()
        return self.dialog_tree.get_target_dialog(dialog_name)

    def dialog_reply(self, dialog_name, clear=False, target_dialog=None):
        self.clear_prompt_text(clear)

        responses = self.dialog_tree.get_responses(dialog_name)
        count = 1
        if not responses is None:
            for response in responses:
                if 'say' in response:
                    self.append_prompt_text(str(count)+". " + response['say'])
                    self.blank_line()
                    count += 1
            no_replies = len(responses)
            self.blank_line(2)
            self.append_prompt_text('Select a reply (enter 1 - '+str(no_replies)+': ')
            self.update()
            response = self.GetChoice()


    def unload(self):
        self.dialog_con.consoloe_delete()

    def get_reply(self, num_responses, tries):
        prompt_text = '\r\n'
        if tries == 1:
            prompt_text += "Select reply:\r\n"
        elif tries <= 3:
            prompt_text += "Please select a response: 1 - " + str(num_responses)+ "\r\n"
        else:
            return 0
        self.append_prompt_text(prompt_text)
        ##selection = self.GetChoice()
        ##print(selection)

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

    def update(self):
        self.add_border()
        libtcod.console_print_rect(self.dialog_con,1,1, self.width-2, self.height, self.prompt_text)
        libtcod.console_blit(self.dialog_con,0, 0,0,0, self.target_con,self.x, self.y )

    def append_prompt_text(self,formatted_text):
        self.prompt_text += formatted_text
        self.update()

    def blank_line(self, count=1):
        for i in range(count):
            self.append_prompt_text("\r\n")

    def clear_prompt_text(self, clear=True):
        if clear:
            self.prompt_text = ''
        self.update()

    def add_border(self):
        libtcod.console_hline(self.dialog_con,0,0,self.width)
        libtcod.console_vline(self.dialog_con,0,0,self.height)
        libtcod.console_hline(self.dialog_con,0,self.height-1,self.width)
        libtcod.console_vline(self.dialog_con,self.width-1,0,self.height)

    def clear(self):
        libtcod.console_clear(self.dialog_con)
