import operator
from utils import test_dict, map_npc_db

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
