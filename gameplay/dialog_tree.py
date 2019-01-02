import operator

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

class DialogTree:

    def __init__(self,dialog_dict=test_dict):
        self.dialog_dict = dialog_dict
        self.loaded_entry = ''


    def get_say(self,dialog_name):
        if self.dialog_exists(dialog_name):
            dialog = self.dialog_dict[dialog_name]
            if 'say' in dialog:
                return dialog['say']
        else:
            return None
    def get_target_dialog(self,dialog_name):

        if self.dialog_exists(dialog_name):
            dialog = self.dialog_dict[dialog_name]
            if 'target_dialog' in dialog:
                return dialog['target_dialog']
        return None

    def get_responses(self, dialog_name):
        if self.dialog_exists(dialog_name):
            dialog = self.dialog_dict[dialog_name]
            if 'response' in dialog:
                return dialog['response']

        return None

    def dialog_exists(self, dialog_name):
        ##Check to see if a dialog name exists in currently loaded dialog tree.
        ##Special case for exit to always return false.
        if dialog_name is None:
            return False
        elif dialog_name == "exit":
            return False
        elif dialog_name in self.dialog_dict:
            return True
        else:
            return False
