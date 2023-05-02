#test enviroment for the combat system
import random
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



# class Enemy: #Broad class for all the enemies then sub classes for each enemy type.
#     def __init__(self, name, stamina, attack, defense, health):
#         self.name = name
#         self.stamina = stamina
#         self.attack = attack
#         self.defense = defense
#         self.health = health

# class Robber(Enemy):#sub class of enemy 
#     def __init__(self, name):
#         super().__init__(name, 80, 80, 80, 80)#super allows inherit the attributes from the enemy class, more info https://realpython.com/python-super/

class Robber:
    def __init__(self, name, stamina, attack, defense, health):
        self.name = name
        self.stamina = stamina
        self.attack = attack
        self.defense = defense
        self.health = health
    


Knight = Character("Ed", 80,80,80,80,) #Creats an instance of the two classes so they can be passed into function
Enemy = Robber("Rob", 80,80,80,80)


def combat(player, Enemy): #credit for idea https://www.youtube.com/watch?v=8F2MAJEeKjw
    print(f"{player.name} v {Enemy.name}")
    while player.health > 0 and Enemy.health > 0:
        
        print("Attack [1]")
        print("Defend [2]")
        print("Run [3]")
        choice = int(input("What do you want to do? "))
        if choice == 1:
            player_Attack = random.randint(player.attack - 10, player.attack + 10)
            Enemy_defense = random.randint(Enemy.defense - 10, Enemy.defense + 10)
            if player_Attack > Enemy_defense:
                Enemy.health = Enemy.health - player_Attack
                if Enemy.health <= 0:
                    print(f"You killed {Enemy.name}  dealing {player_Attack} damage")
                elif Enemy.health > 0:
                    print(f"You dealt {player_Attack} damage to {Enemy.name}")
                    print(f"{Enemy.name} has {Enemy.health} health left")
            elif player_Attack < Enemy_defense:
                print(f"{Enemy.name} blocked your attack")
                Enemy.defense = Enemy.defense - player_Attack



combat(Knight, Enemy)