from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    @abstractmethod
    def attack(self):
        pass

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} received {amount} dmg. Health left: {self.health}")
