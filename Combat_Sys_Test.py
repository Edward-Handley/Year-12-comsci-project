#test enviroment for the combat system

def Enemy(name, health, attack, defense):   
    #function to assign the current enemy 
    enemy = name(health, attack, defense)


class Character:
    def __init__(self, name, stamina, attack, defense, health):
        self.name = name
        self.stamina = stamina
        self.attack = attack
        self.defense = defense
        self.health = health

    def display_stats(self):
        print("Character Name: ", self.name)
        print("Stamina: ", self.stamina)
        print("Attack: ", self.attack)
        print("Defense: ", self.defense)
        print("Health: ", self.health)

    def update_attributes(self, stamina, attack, defense, health): # self.stamina + stamina because otherwise it would override
        self.stamina =  self.stamina + stamina
        self.attack = self.attack + attack
        self.defense = self.defense + defense
        self.health = self.health + health



class Enemy: #Broad class for all the enemies then sub classes for each enemy type.
    def __init__(self, name, stamina, attack, defense, health):
        self.name = name
        self.stamina = stamina
        self.attack = attack
        self.defense = defense
        self.health = health

class Robber(Enemy):#sub class of enemy 
    def __init__(self, name):
        super().__init__(name, 80, 80, 80, 80)#super allows inherit the attributes from the enemy class, more info https://realpython.com/python-super/




Knight = Character("Ed", 80,80,80,80,) #Creats an instance of the two classes so they can be passed into function
enemy = Robber("Rob")


def combat(player, enemy): #credit for idea https://www.youtube.com/watch?v=8F2MAJEeKjw
    print(f"{player.name} v {enemy.name}")


combat(Knight, Robber)