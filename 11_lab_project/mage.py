from character import Character

class Mage(Character):
    def __init__(self, name, health, damage, mana):
        super().__init__(name, health, damage)
        self.mana = mana

    def attack(self):
        if self.mana >= 10:
            print(f"{self.name} casts Fireball: {self.damage} damage!")
            self.mana -= 10
        else:
            print(f"{self.name} doesn't have enough mana to attack!")
        print(f"Mana remaining: {self.mana}")