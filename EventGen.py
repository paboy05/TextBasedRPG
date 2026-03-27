#EventGeneration.py

import random
from Actors import player, Enemy

def player_combat_action(enemy):
    action = input("What do you do? (attack/run): ").lower()
    if action == "attack":
        # Player attacks enemy
        damage = player.attack
        enemy.take_damage(damage)
        if enemy.hp <= 0:
            print(f"{enemy.name} has been defeated!")
            return True # Enemy defeated
        else:
            # Enemy counterattacks
            print(f"{enemy.name} counterattacks!")
            player.take_damage(enemy.attack)
            return False # Combat continues
            
    elif action == "run":
        # Attempt to flee
        if random.random() < 0.5: # 50% chance of successfully getting away
            print("You successfully fled the combat!")
            return True # Combat ends
        else:
            print("You've failed to flee! The enemy attacks you as you try to escape.")
            player.take_damage(enemy.attack)
            return False # Combat continues
    else:
        print ("Invalid action. Please choose 'attack' or 'run'.")
        return False # Combat continues
    
def handle_event(player):
    
    events = ["enemy", "loot", "nothing"]
    current_event = random.choice(events)

    if current_event == "enemy":
        # Create an enemy instance
        enemy = Enemy("Goblin", 10, 3)
        print(f"An aggressive {enemy.name} appears with {enemy.hp} HP and {enemy.attack} attack power!")

        # Combat loop
        while enemy.hp > 0 and player.hp > 0:
            result = player_combat_action(enemy)
            if result:
                break
        if player.hp <= 0:
            print("You have been defeated! Game over!")

    elif current_event == "loot":
        print("You have found a potion in a rotten chest! You drink it and restore 10 HP.")
        # Heal the player / first loot item
        player.hp += 10
        print(f"You now have {player.hp} HP.")

    else:
        print("Nothing happened! You continue on your journey.")