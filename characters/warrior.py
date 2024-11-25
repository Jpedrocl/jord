from .base_characters import Character
import random

class Warrior(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.strength = 10

    def attack(self):
        return random.randint(1, 6) + self.strength
