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

    


def main():
    
    Pcharacter = Create_Character()
    
    want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
    while want_Intro != "Y" and want_Intro != "N":
        print("Invalid entry try again")
        want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
    if want_Intro == "Y":
        Intro()
    else:
        print("No intro, Good luck!")
    



    print(f"Your character is Knight{Pcharacter.name} game will now begin....... good luck ")
  
  
    forrest_result, combat_result = Forrest(Pcharacter)
    #Combat Result returning "None" need to fix this 
   



    #Combat(Pcharacter, enemy)

main()

