from random import randint
from ability import Ability


class Weapon(Ability):

    def attack(self):
        """Return a random value (half - full attack power) of the weapon."""
        attack_value = randint(int(self.max_damage)//2,int(self.max_damage))
        return attack_value