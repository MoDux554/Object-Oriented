class Enemies:

    weapons = {"Gun": 20, "Knife":15, "Poison":10}

    def __init__(self,name,clan,ability):
        self.name = name
        self.clan = clan
        self.ability = ability


    def set_description(self, description):
        self.description = description
        pass

    def get_description(self):
        return self.description


    def set_weapon(self, weapon):
        self.weapon = weapon




enemy1 = Enemies("Grunt", "A", "Super strength")
enemy1.set_description("This enemy has four arms, it looks like it can multi task")
enemy1.set_weapon("Gun")


enemy2 = Enemies("Bodyguard", "B", "Regeneration")
enemy2.set_description("This enemy looks pretty average.")
enemy2.set_weapon("Knife")