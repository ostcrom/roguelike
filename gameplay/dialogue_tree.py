
import json

test_dict = {"main":{
    "say": "Hi there this top level dialogue!",
    "response":[{"say":"Thank you! Whats next?", "target_dialogue":"answer_happy"},
            {"say":"Get that corn outta my face!", "target_dialogue":"answer_indignant"}]
    },
    "answer_happy":{
        "say":["Well, how about I invite you to finished basement apartment,",
        "located conveniently under my parents house. I have imitation",
        "crab meat to share!"],
        "emote":"You back away slowly.",
        "target_dialogue":"exit"
    },
    "answer_indignant":{
        "say":["If my the elastic hadn't broken on my stretchy pants, I would",
        "kick your ass."],
        "emote":"You are chased away by cheetos covered fingers.",
        "target_dialogue":"exit"
    }
}

class DialogueTree:

    def __init__(self,dialogue):
        print(json.dumps(dialogue))


diag = DialogueTree(test_dict)
