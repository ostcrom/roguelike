import operator
from utils import test_dict, map_npc_db

class DialogTree:

    def __init__(self,dialog_dict=test_dict):
        self.dialog_dict = dialog_dict
        self.loaded_entry = ''


    def get_say(self,dialog_name):

        if self.dialog_exists(dialog_name):
            dialog = self.dialog_dict[dialog_name]
            return dialog.get('say', None)

        return None
    
    def get_target_dialog(self,dialog_name):

        if self.dialog_exists(dialog_name):
            dialog = self.dialog_dict[dialog_name]
            return dialog.get('target_dialog', None)

        return None

    def get_conditions(self,dialog_name):
        if self.dialog_exists(dialog_name):
            dialog = self.dialog_dict[dialog_name]
            return dialog.get('conditions', None)
        return None

    def get_responses(self, dialog_name):
        if self.dialog_exists(dialog_name):
            dialog = self.dialog_dict[dialog_name]
            if 'response' in dialog:
                return dialog.get('response')

        return None

    def dialog_exists(self, dialog_name):
        ##Check to see if a dialog name exists in currently loaded dialog tree.
        ##Special case for exit to always return false.
        if dialog_name == "exit":
            return False
        elif dialog_name in self.dialog_dict:
            return True
        else:
            return False
