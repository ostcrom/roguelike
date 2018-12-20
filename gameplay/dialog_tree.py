import json
import operator


test_dict = {"main":{
    "say": "Hi there this top level dialog!",
    "response":[{"say":"Thank you! Whats next?", "target_dialog":"answer_happy"},
            {"say":"Get that corn outta my face!", "target_dialog":"answer_indignant"},
            {"say":"Can I have the dialog tutorial?","target_dialog":"example_dialog"}],
    },
    "answer_happy":{
        "say":["Well, how about I invite you to my finished basement apartment,",
        "located conveniently under my parents house. I have imitation",
        "crab meat to share!"],
        "emote":["You back away slowly."],
        "target_dialog":"exit"
    },
    "answer_indignant":{
        "say":["If the elastic hadn't broken in my stretchy pants, I would",
        "kick your ass."],
        "target_dialog":"exit"
    },

    "example_dialog":{
        "say":["This example dialog will provide a dialog object with all",
                "possible keys and demonstrate the order dialog objects",
                "are processed in, which is respective to the order found",
                "within this code. IE: The 'say' key is processed first,",
                "followed by the response key."],
        "response":[{"say":"I think that makes sense.", "target_dialog":"answer_happy"},
                    {"say":"I like turtles and nested json objects", "target_dialog":"answer_indignant"}]
    }
}

class DialogTree:

    def __init__(self,dialog_dict):
        self.dialog_dict = dialog_dict
        self.dialog = {}

    def load_dialog(self, dialog_name):
        ##TODO Scriptable interface probably needs robust input checking.
        if dialog_name == 'exit':
            return

        dialog = self.dialog_dict[dialog_name]

        if 'say' in dialog:
            self.say_line (dialog['say'])

        if 'response' in dialog:
            responses = dialog['response']
            num_responses = len(responses)
            print ('')
            player_select = 1

            for response in responses:
                if 'say' in response:
                     self.say_line(str(player_select) +".  - " +response['say'])
                player_select += 1

            selection_index = self.get_reply(num_responses, 1)

            if 'target_dialog' in responses[selection_index]:
                self.load_dialog(responses[selection_index]['target_dialog'])

        if 'emote' in dialog:
                self.say_line("*** "+ dialog['emote'] +" ***")

        if 'target_dialog' in dialog:
            target_dialog = dialog['target_dialog']
            self.load_dialog(target_dialog)

    def get_reply(self, num_responses, tries):
        if tries == 1:
            print ("Select reply:")
        elif tries <= 3:
            print ("Please select a response: 1 - " + str(num_responses))
        selection = int(input("\t"))
        if tries > 3:
            return 0;
        elif not selection < 1 and not selection > num_responses:
            ##Numbers displayed for player use human counting. Subtract one so
            ##we get the appropriate array index.
            return selection - 1;
        else:
            return self.get_reply(num_responses, tries + 1)
    ##Methods to be super imposed by inheriting object.
    def say_line(self, line):
        print(line)

    def reply_line(self,line):
        print(line)
