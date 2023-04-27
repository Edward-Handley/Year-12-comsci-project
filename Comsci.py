import random
import time



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
    def __init__(self):
        super().__init__("Rob the Robber", 80, 80, 80, 80)#super allows inherit the attributes from the enemy class, more info https://realpython.com/python-super/


        


def Intro():
    print("\n \n \n")
    print("You are a brave knight who is trying to return home from an epic battle")
    print("You have been travelling for days and are now in a forest \n you must play to your strengths to defeat enemies in three different areas")
    print("The frightening forest")
    print("The hostile vilage")
    print("The trecherous marsh lands")
    print("Once you do all these you can return home to your kingdom")
    print("Good luck")


def Create_Character():
    name = input("What shall your knight be called? ")
    Knight = Character(name, 80,80,80,80,)
    print(f"Knight {name}, wonderfull name")    
    print("As a knight you have 4 attributes")
    print("Stamina, Attack, Defense and Health")
    print("All start at a level of 80, you can now spend 20 points to upgrade your stats")
    start = input("Read to start [Y/N] ").upper()
    if start != "Y" or "N":
        print("Invalid entry please try again")
        start = input("Read to start [Y/N]").upper()
    while start != "Y":
        start = input("When you are ready to start type Y")
    points_to_spend = 20
    while points_to_spend > 0:
        print(f"You have {points_to_spend} points to spend")
        stamina = int(input(f"Your current stamina is {Knight.stamina}, how many points would you like to spend on Stamina? "))
        while stamina > points_to_spend:
            print("You don't have enough points to spend")
            stamina = int(input(f"Your current stamina is {Knight.stamina}, how many points would you like to spend on Stamina? "))
        print(f"Great {stamina} points added to stamina. You have {points_to_spend - stamina} points left")
        
        points_to_spend = points_to_spend - stamina
        attack = int(input(f"Your current attack is {Knight.attack}, how many points would you like to spend on Attack? "))
        while attack > points_to_spend:
            print("You don't have enough points to spend")
            attack = int(input(f"Your current attack is {Knight.attack}, how many points would you like to spend on Attack? "))
        print(f"Great {attack} points added to attack. You have {points_to_spend - attack} points left")
        
        points_to_spend = points_to_spend - attack
        defense = int(input(f"Your current defense is {Knight.defense}, how many points would you like to spend on Defense? "))
        while defense > points_to_spend:
            print("You don't have enough points to spend")
            defense = int(input(f"Your current defense is {Knight.defense}, how many points would you like to spend on Defense? "))
        print(f"Great {defense} points added to defense. You have {points_to_spend - defense} points left")

        points_to_spend = points_to_spend - defense
        health = int(input(f"Your current health is {Knight.health}, how many points would you like to spend on Health? "))
        while health > points_to_spend:
            print("You don't have enough points to spend")
            health = int(input(f"Your current health is {Knight.health}, how many points would you like to spend on Health? "))
        print(f"Great {health} points added to health. You have {points_to_spend - health} points left")
        points_to_spend = points_to_spend - health
    
    Knight.update_attributes(stamina, attack, defense, health)
    print("╔═════════════════════╦════════════════╗")
    print("║          CHARACTER ATTRIBUTES        ║")
    print("╠═════════════════════╬════════════════╣")
    Knight.display_stats()



# class Robbers():
#     def __init__(self, name, health, attack, defense):
#         self.name = "Rob the Robber"
#         self.health = health
#         self.attack = attack
#         self.defense = defense
    
#     def display_stats(self):
#         print("Character Name: ", self.name)
#         print("Attack: ", self.attack)
#         print("Defense: ", self.defense)
#         print("Health: ", self.health)
    

def Enemy(name, health, attack, defense):   
    #function to assign the current enemy 
    enemy = name(health, attack, defense)

def Forrest():
    print("You are now in the forest, you are surrounded by trees with a sole gravel footpath leading through the forest \n this parth leeds to the exit")
    print("However you know that in the forrest lurks many dangerous creatures, you must be careful")

    # put a ascii art when decisenio segment
    run_or_walk = input("Feeling uneasy about the forrest you begin moveing towards the exit, do you chose to run [R] or walk [W]?").upper()
    while run_or_walk not in ["R", "W"]:
        print("Invalid entry, please try again")
        run_or_walk = input("Feeling uneasy about the forrest you begin moveing towards the exit, do you chose to run [R] or walk [W]?").upper()
    if run_or_walk == "R":
        print("You begin to run, you are making good progress and are nearly at the exit when a robber sprins out onto the path")
        print("You have no choice but to fight")

        
def combat(enemy, knight):
    #
    print(f"{enemy.name}")  
    
    




def main():
    print("Welcome to .... game")
    print("First you have to make your character \n \n")
    Create_Character()

    
    intro = input("Do you want an intro to the game? [Y/N]").upper()
    while intro not in ["Y", "N"]:
        print("Invalid entry, please try again")
        intro = input("Do you want an intro to the game? [Y/N] ")

    if intro == "Y":
        Intro()
    else:
        print("Good luck")
    print("\n \n \n \n")

    # print("You are now in the forest")
    # print("With tall trees blocking out any light ....")
    # print("You are stood on a gravel track, you can see the")
        

main()











