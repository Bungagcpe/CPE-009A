#Charcater
class Character():
    def __init__(self, username):
        self.__username = username
        self.__hp = 100
        self.__mana = 100
        self.__damage= 5
        self.__strenght = 0
        self.__vitality = 0
        self.__intelligence = 0
        self.__agility = 0
    def getUsername(self):
        return self.__username
    def setUsername(self, new_username):
        self.__username = new_username
    def getHp(self):
        return self.__hp
    def setHp(self, new_hp):
        self.__hp = new_hp
    def getMana(self):
        return self.__mana
    def setMana(self, new_mana):
        self.__mana = new_mana
    def getDamage(self):
        return self.__damage
    def setDamage(self, new_damage):
        self.__damage = new_damage
    def getStrenght(self):
        return self.__strenght
    def setStrength(self, new_strenght):
        self.__strenght = new_strenght
    def getVitality(self):
        return self.__vitality
    def setVitality(self, new_vitality):
        self.__vitality = new_vitality
    def getIntelligence(self):
        return self.__intelligence
    def setIntelligence(self, new_intelligence):
        self.__intelligence = new_intelligence
    def getAgility(self):
        return self.__agility
    def setAgility(self, new_agility):
        self.__agility = new_agility
    def reduceHp(self, damage_amount):
        self.__hp = self.__hp - damage_amount
    def addHp(self, heal_amount):
        self.__hp = self.__hp + heal_amount
character1 = Character("Zelensk")
print(character1.getUsername())
#An error occured because 'Character' object has no attribute '__username'.
#To fix this, I tried to cut the functions in setting the attributes, and then ran the code to see if it works on the function stored in the Character.
#Then I pasted the main functions for attributes and it works.