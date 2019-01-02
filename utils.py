def color_tag_string(color):
    return "[color="+color+"]"

test_dict = {
    "main":{
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

npc_dialog_db = {
    "Character Name" : {
        "default" : test_dict,
        "second_dialog" : test_dict
    },

    "Danny Davis" : {
        "default" : test_dict
    }
}

map_npc_db = {
    "Ground Floor":{},
    "Basement":{"Danny Davis":{
    "type" : "npc",
    "x" :17,
    "y": 21,
    "dialog":"default"
    }},
    "Basement 2":{}
}
