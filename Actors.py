#player.py

class player:
    def __init__(self):
        self.name = "Hero"
        self.hp = 20
        self.attack = 5
        self.inventory = []

player = player()

#enemy.py

class enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack