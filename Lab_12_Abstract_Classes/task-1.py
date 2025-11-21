from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def move(self):
        pass
class dog(animal):
    def move(self):
        return "На четверенках"
    def make_sound(self):
        return "Гав-гав"
class cat(animal):
    def move(self):
        return "На четверенках"
    def make_sound(self):
        return "мяу-мяу"
class bird(animal):
    def move(self):
        return "По воздуху"
    def make_sound(self):
        return "чик чик"
class fish(animal):
    def move(self):
        return "по воде"
    def make_sound(self):
        return "буль-буль"
animal = [dog(),cat(),bird(),fish()]

for v in animal:
    print(f"{v.__class__.__name__}: {v.move()} — make-sound: {v.make_sound()}")