from warrior import Warrior
from mage import Mage
from archer import Archer

characters = [
    Warrior("Ivar", 120, 25),
    Mage("Nukkich", 80, 40, mana=30),
    Archer("Din", 90, 20, arrows=3)
]

for ch in characters:
    ch.attack()