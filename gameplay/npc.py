from game_object import GameObject
from gameplay.dialog_tree import DialogTree
from utils import npc_dialog_db

class NPC(GameObject):
    def __init__(self, x, y, char, color, name, dialog_name='default'):
        super().__init__(self, x, y, char, color, name, True)
        self.dialog_dict = {}
        self.load_dialog(dialog_name)
    def load_dialog(self, dialog_name):
        ##Returns True on successfull load
        if self.name in npc_dialog_db:
            npc_branch = npc_dialog_db[self.name]
            if dialog_name in npc_branch:
                self.dialog_dict = npc_branch[dialog_name]
                return True

        ##if load fails, attempts to load the default dialog via recursion
        ##but finally return false if that fails
        self.dialog_dict = None
        if not dialog_name == "default":
            return self.load_dialog('default')
        else:
            return False
