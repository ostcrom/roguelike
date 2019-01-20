import operator

def color_tag_string(color):
    return "[color="+color+"]"

test_dict = {
    "main":{
    "say": "Hi there this is an example of top level dialog!",
    "response":[{"say":"Thank you! Whats next?", "target_dialog":"answer_happy"},
            {"say":"Get that corn outta my face!", "target_dialog":"answer_indignant"},
            {"say":"Can I have the dialog tutorial?","target_dialog":"example_dialog"}],
    "target_dialog":"example_dialog",
    "conditions" : [
        {"condition_string" : "item = Goblet",
            "failed_target_dialog" : "falied1"}
    ]
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
    },
    "failed1" : {
        "say" : "You don't look like a hero to me!",
        "target_dialog" : "exit"
    }
}

npc_dialog_db = {
    "Character Name" : {
        "default" : test_dict,
        "second_dialog" : test_dict
    },

    "Danny Davis" : {
        "default" : test_dict
    }
}

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


map_npc_db = {
    "Basement":{},
    "Ground Floor":{"Danny Davis":{
    "type" : "npc",
    "x" :6,
    "y": 3,
    "dialog":"default"
    }},
    "Basement 2":{}
}

## https://stackoverflow.com/questions/18591778/how-to-pass-an-operator-to-a-python-function
def get_truth(first_var, operator_symbol, second_var):
    ops = {'>': operator.gt,
           '<': operator.lt,
           '>=': operator.ge,
           '<=': operator.le,
           '=': operator.eq}
    return ops[operator_symbol](first_var, second_var)
