from .base_characters import Character
import random

class Archer(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.dexterity = 8

    def shoot(self):
        return random.randint(1, 6) + self.dexterity
