#main.py

from random import random

from Actors import player
from EventGen import player_combat_action
import EventGen


def main():

    print("Welcome to the Text-Based RPG!")

    while player.hp > 0:
        EventGen.handle_event(player)

    # More game logic

    print ("Game over! Thanks for playing!")

if __name__ == "__main__":
    main()