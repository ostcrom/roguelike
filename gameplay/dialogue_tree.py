import json

test_dict = {"main":{
    "say": ["Hi there this top level dialogue!"],
    "response":[{"say":"Thank you! Whats next?", "target_dialogue":"answer_happy"},
            {"say":"Get that corn outta my face!", "target_dialogue":"answer_indignant"}],
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

    def load_dialogue(self, dialogue_name):
        ##TODO Scriptable interface probably needs robust input checking.
        if dialogue_name == 'exit':
            return

        dialogue = self.dialogue_dict[dialogue_name]

        if 'say' in dialogue:
            for line in dialogue['say']:
                print (line)

        if 'response' in dialogue:
            responses = dialogue['response']
            num_responses = len(responses)
            print ('')
            player_select = 1
            for response in responses:
                if 'say' in response:
                     print(str(player_select) +".  - " +response['say'])
                player_select += 1
            selection_index = self.get_reply(num_responses, 1)
            if 'target_dialogue' in responses[selection_index]:
                self.load_dialogue(responses[selection_index]['target_dialogue'])
        if 'target_dialogue' in dialogue:
            target_dialogue = dialogue['target_dialogue']
            self.load_dialogue(target_dialogue)
    def get_reply(self, num_responses, tries):
        if tries == 1:
            print ('\n Select reply:')
        elif tries <= 3:
            print ("\n Please select a response: 1 - " + str(num_responses))
        selection = int(input())
        if tries > 3:
            return 0;
        elif not selection < 1 and not selection > num_responses:
            ##Numbers displayed for player use human counting. Subtract one so
            ##we get the appropriate array index.
            return selection - 1;
        else:
            return self.get_reply(num_responses, tries + 1)
DialogueTree(test_dict)
