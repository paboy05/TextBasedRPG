from asyncio import events
from random import random

from Actors import player
from EventGen import player_combat_action

def main():
   
    while player.hp > 0:
        event = random.choice(events)
    if event == "enemy":
        print ("An enemy appears!")
       
        #Ask for player action--
        player_combat_action()

    elif event == "treasure":
        # give loot
        pass
    else:
        print("Nothing Happened!")