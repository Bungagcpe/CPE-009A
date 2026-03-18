from Novice import Novice

class Magician(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setIntelligence(10)
        self.setVitality(5)
        self.setHp(self.getHp()+self.getVitality())

    def heal(self):
        self.addHp(self.getIntelligence())
        print(f"{self.getUsername()} Healing for you!+{self.getIntelligence()}")

    def magicAttack(self, character):
        self.new_damage = self.getDamage()+self.getIntelligence()
        character.reduceHp(self.new_damage)
        print(f"{self.getUsername()} performed Magic Attack!-{self.new_damage}")