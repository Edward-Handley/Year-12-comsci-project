# from Characters.Characters import Character, Enemy
# from Game_Functions.Intro_func import *
# from Game_Functions.Combat import *


# def main():
#     # Your main function here
#     player = Create_Character()
#     # ...
#     forrest_result, combat_result = Forrest(player)

#     # Continue with the rest of the game


# main()

import random

# from Characters.Characters import Character, Robber
# from Game_Functions.Combat import Combat


def Intro():
    print("\n \n \n")
    print("You are a brave knight who is trying to return home from an epic battle")
    print("You have been travelling for days and are now in a forest \n you must play to your strengths to defeat enemies in three different areas")
    print("The frightening forest")
    print("The hostile vilage")
    print("The trecherous marsh lands")
    print("Once you do all these you can return home to your kingdom")
    print("Good luck")



# def Forrest():
#     print("You start you journey in a descriptive on a narrow gravel path")
#     run_or_walk = int(input("You see exit, run [1] or walk [2]"))
#     if run_or_walk == 1:
#         print("you begin to run for the exit, your footsteps crunch the gravel....")
#         print("Just before you reach the exit a robber appears, you must fight him to get throught")
#         choice = "run"
#     else:
#         print("you sneek past")
#         choice = "walk"
    
#     return choice

def Forrest(player):
    print("You start your journey in a descriptive on a narrow gravel path")
    run_or_walk = int(input("You see exit, run [1] or walk [2]"))
    if run_or_walk == 1:
        print("you begin to run for the exit, your footsteps crunch the gravel....")
        print("Just before you reach the exit a robber appears, you must fight him to get through")
        choice = "run"
    else:
        print("As you sneak past, you notice a movement in the bushes...")
        print("A robber appears, you must fight him to get through")
        choice = "walk"

    robber = Robber("Robber", 80, 80, 80, 80)
    combat_result = Combat(player, robber)

    return choice, combat_result



# import random

# from Characters.Characters import Character, Robber
# from Game_Functions.Combat import Combat


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



#Module for all function concering the character

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



def Create_Character():
    name = input("What shall your knight be called? ")
    Base_Character = Character(name, 80,80,80,80,)
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
        stamina = int(input(f"Your current stamina is {Base_Character.stamina}, how many points would you like to spend on Stamina? "))
        while stamina > points_to_spend:
            print(f"You don't have enough points to spend, {points_to_spend} left")
            stamina = int(input(f"Your current stamina is {Base_Character.stamina}, how many points would you like to spend on Stamina? "))
        print(f"Great {stamina} points added to stamina. You have {points_to_spend - stamina} points left")
        
        points_to_spend = points_to_spend - stamina
        attack = int(input(f"Your current attack is {Base_Character.attack}, how many points would you like to spend on Attack? "))
        while attack > points_to_spend:
            print(f"You don't have enough points to spend, {points_to_spend} left")
            attack = int(input(f"Your current attack is {Base_Character.attack}, how many points would you like to spend on Attack? "))
        print(f"Great {attack} points added to attack. You have {points_to_spend - attack} points left")
        
        points_to_spend = points_to_spend - attack
        defense = int(input(f"Your current defense is {Base_Character.defense}, how many points would you like to spend on Defense? "))
        while defense > points_to_spend:
            print(f"You don't have enough points to spend, {points_to_spend} left")
            defense = int(input(f"Your current defense is {Base_Character.defense}, how many points would you like to spend on Defense? "))
        print(f"Great {defense} points added to defense. You have {points_to_spend - defense} points left")

        points_to_spend = points_to_spend - defense
        health = int(input(f"Your current health is {Base_Character.health}, how many points would you like to spend on Health? "))
        while health > points_to_spend:
            print(f"You don't have enough points to spend, {points_to_spend} left")
            health = int(input(f"Your current health is {Base_Character.health}, how many points would you like to spend on Health? "))
        print(f"Great {health} points added to health. You have {points_to_spend - health} points left")
        points_to_spend = points_to_spend - health
    
    
    
    
    Base_Character.update_attributes(stamina, attack, defense, health)
    return Base_Character



    print("╔═════════════════════╦════════════════╗")
    print("║          CHARACTER ATTRIBUTES        ║")
    print("╠═════════════════════╬════════════════╣")
    Base_Character.display_stats()
  




class Robber:
    def __init__(self, name, stamina, attack, defense, health):
        self.name = name
        self.stamina = stamina
        self.attack = attack
        self.defense = defense
        self.health = health
    


def test():
    #Begging
    Pcharacter = Create_Character()
    Pstats = Character()
    #Pcharacter = Character("ed", 80, 80, 80, 80) #just test data

    
   # Pcharacter = Character(name, stamina, attack, defense, health)
    #Pstats = Pcharacter.get_stats()
    want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
    while  want_Intro not in "Y" or "N":
        print("Invalid entry ry again")
        want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
    if want_Intro == "Y":
        Intro()
    else:
        print("No intro, Good luck!")

    print(f"Your character {Pcharacter.name} ")
    enemy = Robber("Robber", 80, 80, 80, 80) #create instance of enemy for forrest section 
    # run_or_Walk = Forrest()
    # print(run_or_Walk)
    # if run_or_Walk == "run":
        
        
    #Combat_winner = Combat(Pstats, enemy)
    forrest_result, combat_result = Forrest(Pcharacter)



    #Combat(Pcharacter, enemy)

test()