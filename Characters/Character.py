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
  