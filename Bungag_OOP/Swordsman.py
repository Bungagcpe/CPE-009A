from Novice import Novice

class Swordsman(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setStrength(5)
        self.setVitality(10)
        self.setHp(self.getHp()+self.getVitality())

    def slashAttack(self, character):
        self.new_damage = self.getDamage()+self.getStrenght()
        character.reduceHp(self.new_damage)
        print(f"{self.getUsername()} performed Slash Attack! - {self.new_damage}")
