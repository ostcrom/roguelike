
import json

test_dict = {"main":{
    "say": "Hi there this top level dialogue!",
    "response":[{"say":"Thank you! Whats next?", "target_dialogue":"answer_happy"},
            {"say":"Get that corn outta my face!", "target_dialogue":"answer_indignant"}]
    },
    "answer_happy":{
        "say":["Well, how about I invite you to my finished basement apartment,",
        "located conveniently under my parents house. I have imitation",
        "crab meat to share!"],
        "emote":"You back away slowly.",
        "target_dialogue":"exit"
    },
    "answer_indignant":{
        "say":["If the elastic hadn't broken in my stretchy pants, I would",
        "kick your ass."],
        "target_dialogue":"exit"
    }
}

class DialogueTree:

    def __init__(self,dialogue_dict):
        self.dialogue_dict = dialogue_dict
        self.dialogue = {}

        self.load_dialogue('main')

    def load_dialogue(self,dialogue_name):
        self.dialogue.clear()
        self.dialogue = self.dialogue_dict.get('dialogue_name')
