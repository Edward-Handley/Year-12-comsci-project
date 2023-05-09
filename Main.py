from Characters.Characters import *
from Game_Functions.Intro_func import *
import random
import rich



class Robber:
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

    


def Combat(player, enemy):
    
        P_attack = player.attack
        E_attack = enemy.attack
        P_defense = player.defense
        E_defense = enemy.defense

        print(f"Combat between {player.name} and {enemy.name}")
        turn = "p"
        while player.health > 0 and enemy.health >0:
            
            if turn == "p":
                P_move = int(input("Do you want to attack[1] or defend[2] \n Enter here: "))
                if P_move == 1:
                    P_attack_chance = player.attack * random.uniform(0.8, 1.2) > enemy.defense * random.uniform(0.1,1)
                    if P_attack_chance: #True or False
                        P_damage = enemy.health
                        print(f"You hit {enemy.name} for {P_damage} insta killing")
                        enemy.health -= P_damage
                    else:
                        print(f"You missed your attack")
                elif P_move == 2:
                    P_defense_chance = player.defense * random.uniform(0.8, 1.2) > enemy.attack * random.uniform(0.1, 1)
                    if P_defense_chance:
                        print("You defend the enemies attack")
                    else:
                        E_damage = random.randint(10,20)
                        print(f"You failed to defend their attack and took {E_damage}")
                        player.health -= E_damage
                turn = "e"
            elif turn =="e":
                print(f"Now it is {enemy.name}'s turn to attack")
                E_attack_chance = E_attack * random.uniform(0.1,1) > P_attack * random.uniform(0.8,1.2)
                if E_attack_chance:
                    E_damage = random.randint(E_attack, player.health)
                    print(f"{enemy.name} hit you for {E_damage} you have {player.health - E_damage} health left")
                    player.health -= E_damage
                else:
                    print(f"{enemy.name} missed their attack on you")
        if enemy.health <= 0:
            print(f"You defeated {enemy.name}")
            Combat_result = "win"
        else:
            print(f"you were defeated")
            Combat_result = "lose"

                     
                     
        
        
        
        
        
        
        
     
    

            
        
        






def main():
    #Begging
    Pcharacter = Create_Character()
    #Pstats = Character()
    #Pcharacter = Character("ed", 80, 80, 80, 80) #just test data

    
   # Pcharacter = Character(name, stamina, attack, defense, health)
    #Pstats = Pcharacter.get_stats()
    want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
    while want_Intro != "Y" and want_Intro != "N":
        print("Invalid entry try again")
        want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
    if want_Intro == "Y":
        Intro()
    else:
        print("No intro, Good luck!")


    print(f"Your character {Pcharacter.name} ")
    enemy = Robber("Robber", 80, 80, 80, 80) #create instance of enemy for forrest section 
   
        
        
  
    forrest_result, combat_result = Forrest(Pcharacter)
    



    #Combat(Pcharacter, enemy)

main()

