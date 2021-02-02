import random

enemy_count = 0

class Enemies:

    weapons = {"Gun": 20, "Knife":15, "Poison":10}

    def __init__(self,name,clan,ability):
        self.name = name
        self.clan = clan
        self.ability = ability


    def set_description(self, description):
        self.description = description

    def get_description(self):
        return f""" This enemy's name is {self.name} they are from the {self.clan} clan,
and their ability is: {self.ability} {self.description}"""


    def set_weapon(self, weapon):
        self.weapon = weapon
        self.damage = Enemies.weapons[self.weapon]

    def get_weapon(self):
        return f" Weapon:{self.weapon}, Damage: {self.damage} "



# enemy1 = Enemies("Grunt", "A", "Super strength")
# enemy1.set_description("This enemy has four arms, it looks like it can multi task")
# enemy1.set_weapon("Knife")
# print(enemy1.get_description())
# print(enemy1.get_weapon())
#
#
# enemy2 = Enemies("Bodyguard", "B", "Regeneration")
# enemy2.set_description("This enemy looks pretty average.")
# enemy2.set_weapon("Gun")
# print(enemy2.get_description())
# print(enemy2.get_weapon())
#


list_of_enemies =[]

while enemy_count<5:
    list_of_enemies.append(Enemies.weapons)
    enemy_count += 1
    print(list_of_enemies)