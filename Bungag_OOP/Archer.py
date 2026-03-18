from Novice import Novice
import random

class Archer(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setAgility(5)
        self.setIntelligence(5)
        self.setVitality(5)
        self.setHp(self.getHp()+self.getVitality())

    def rangedAttack(self, character):
        self.new_damage = self.getDamage()+random.randint(0, self.getIntelligence())
        character.reduceHp(self.new_damage)
        print(f"{self.getUsername()} performed Slash Attack! - {self.new_damage}")