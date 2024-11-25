from .base_characters import Character
import random

class Mage(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.mana = 10

    def cast_spell(self):
        return random.randint(1, 6) + self.mana
