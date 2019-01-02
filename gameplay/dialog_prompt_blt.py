import libtcodpy as libtcod
import textwrap
from gameplay.dialog_tree import DialogTree
from game_object import GameObject




class DialogPrompt():
    def __init__(self, dialog_dict=test_dict):

        self.dialog_tree = DialogTree(dialog_dict)
        self.wait_for_reply = False
        self.exit = True

    def dialog_say(self, dialog_name):
        return self.dialog_tree.get_say(dialog_name)

    def can_reply(self,dialog_name):
        if 'response' in
