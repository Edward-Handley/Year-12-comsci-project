from Characters.Character import *
from Game_Functions.Intro_func import *
import random



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

        while player.health > 0 and enemy.health >0:
            turn = "p"
            if turn == "p":
                P_move = int(input("Do you want to attack[1] or defend[2] \n Enter here: "))
                if P_move == 1:
                    P_attack_chance = player.attack * random.uniform(0.8, 1.2) > enemy.defense * random.uniform(0.1,1)
                    if P_attack_chance: #True or False
                        P_damage = enemy.health
                        print(f"You hit {enemy.name} for {P_damage} insta killing")
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
                print("follow through")


                     
                     
        
        
        
        
        
        
        
        
        # while player.health > 0 and  enemy.health > 0:
    #     #print(f"{player.health} vs {enemy.health}")
        # P_move = int(input(f"you are entering combat you have 2 options \n [1]Attack \n [2]Run"))
        # if P_move == 1:
        #     print("attack")
        #     if P_attack > E_defense:
        #             #if P_attack - E_defense > For random chance
        #         if P_attack > enemy.health:
        #             print(f"You succesfully hit and defeated {enemy.name}, you dealt {P_attack} damage \n The enemy didnt block any of your attack")
        #         else:
        #             print(f"You succesfully hit  {enemy.name}, you dealt {P_attack} damage \n The enemy didnt block any of your attack")
        #             print(f"They have {enemy.health} left")
        # if P_move == 2:
        #     print("defense")

        #     if P_defense > P_attack:
        #         print("You blocked the enemies attack, this has left them vunerable. You have a chance to critical hit them")
        #         Counter = input(f"Do you want to counter attack \n [1]Yes \n[2]No")
        #         if Counter == 1:
        #             print("test")
    

            
        
        






def main():
    #Begging
    #Pcharacter = Create_Character()
    #Pstats = Character
    Pcharacter = Character("ed", 80, 80, 80, 80) #just test data

    
    #Pcharacter = Character(name, stamina, attack, defense, health)
    # want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
    # while want_Intro != "Y" or "N":
    #     print("Invalid entry ry again")
    #     want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
    # if want_Intro == "Y":
    #     Intro()
    # else:
    #     print("No intro, Good luck!")

    print(f"Your character {Pcharacter.name} ")
    enemy = Robber("Robber", 80, 80, 80, 80)
    
    Combat(Pcharacter, enemy)

main()
