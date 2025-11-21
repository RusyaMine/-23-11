from character import Character

class Warrior(Character):
    def attack(self):
        print(f"{self.name} attacks with a sword: {self.damage} damage!")
