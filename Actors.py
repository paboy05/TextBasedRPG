#player.py

class Player:
    def __init__(self):
        self.name = "Hero"
        self.hp = 20
        self.attack = 5
        self.inventory = []

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} took {damage} damage and now has {self.hp} HP.")

player = Player()



#enemy.py

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} took {damage} damage and now has {self.hp} HP.")

    def attack_player(self, player):
        print(f"{self.name} attacks {player.name} and deals {self.attack} damage!")
        player.take_damage(self.attack)
