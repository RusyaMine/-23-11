from character import Character

class Archer(Character):
    def __init__(self, name, health, damage, arrows):
        super().__init__(name, health, damage)
        self.arrows = arrows

    def attack(self):
        if self.arrows > 0:
            print(f"{self.name} releases an arrow: {self.damage} damage!")
            self.arrows -= 1
        else:
            print(f"{self.name} has no arrows left!")
        print(f"Arrows left: {self.arrows}")