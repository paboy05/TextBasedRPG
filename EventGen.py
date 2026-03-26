
#EventGeneration.py

import random

events = ["enemy", "loot", "nothing"]
current_event = random.choice(events)

def player_combat_action():
    action = input("What do you do? (attack/run): ").lower()
    if action == "attack":
         # calculate damage
        pass
    elif action == "run":
         # attempt escape
        pass

    