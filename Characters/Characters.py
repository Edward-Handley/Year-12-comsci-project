
from rich import print

#Module for all function concering the charater

class Character:
    def __init__(self, name, stamina, attack, defense, health):
        self.name = name
        self.stamina = stamina
        self.attack = attack
        self.defense = defense
        self.health = health
        self.inventory = []

    def display_stats(self): # Shows all player stats
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

class Enemy: #Enemy class
    def __init__(self, name, stamina, attack, defense, health):
        self.name = name
        self.stamina = stamina
        self.attack = attack
        self.defense = defense
        self.health = health
    



def Create_Character():
    name = input("What shall your knight be called? ")
    Base_Character = Character(name, 80,80,80,80,)
    print(f"\n \n \n \nKnight [bold blue] {name} [/bold blue], wonderfull name")    
    print("you have 4 attributes \n [1]Stamina \n [2]Attack \n [3]Defense \n [4]Health")
    print("You can spend [bold blue] 20 [/bold blue] points")
    start = input("Read to start [Y/N] ").upper()
    while start != "Y" and start != "N":
        print("Invalid entry please try again")
        start = input("Read to start [Y/N]").upper()
    while start != "Y":
        start = input("When you are ready to start type Y")
    points_to_spend = 20
    while points_to_spend > 0:
        print(f"You have {points_to_spend} points to spend")
        print(f"\nCurrent stamina: [bold blue]{Base_Character.stamina}[/bold blue]")
        stamina = int(input("How many points would you like to spend on Stamina? "))
      
        while stamina > points_to_spend:
            print(f"You don't have enough points to spend, {points_to_spend} left")
            print(f"\nCurrent stamina: [bold blue]{Base_Character.stamina}[/bold blue]")
            stamina = int(input("How many points would you like to spend on Stamina? "))
        print(f" + {stamina} stamina  [bold red]{points_to_spend - stamina} [/bold red]points left")

          
        
        points_to_spend = points_to_spend - stamina
        print(f"\nCurrent attack: [bold blue]{Base_Character.attack}[/bold blue]")
        attack = int(input("How many points would you like to spend on Attack? "))
        while attack > points_to_spend:
            print(f"You don't have enough points to spend, {points_to_spend} left")
            print(f"\nCurrent attack: [bold blue]{Base_Character.attack}[/bold blue]")
            attack = int(input("How many points would you like to spend on Attack? "))
        print(f" + {attack} stamina  [bold red]{points_to_spend - attack} [/bold red]points left")
        
        
        points_to_spend = points_to_spend - attack
        print(f"\nCurrent attack: [bold blue]{Base_Character.defense}[/bold blue]")
        defense = int(input("How many points would you like to spend on defense? "))
        while defense > points_to_spend:
            print(f"You don't have enough points to spend, {points_to_spend} left")
            print(f"\nCurrent attack: [bold blue]{Base_Character.defense}[/bold blue]")
            defense = int(input("How many points would you like to spend on defense? "))
        print(f" + {defense} stamina  [bold red]{points_to_spend - defense} [/bold red]points left")
        
        
        points_to_spend = points_to_spend - defense
        print(f"\nCurrent attack: [bold blue]{Base_Character.health}[/bold blue]")
        health= int(input("How many points would you like to spend on health? "))
        while health > points_to_spend:
            print(f"You don't have enough points to spend, {points_to_spend} left")
            print(f"\nCurrent attack: [bold blue]{Base_Character.health}[/bold blue]")
            health= int(input("How many points would you like to spend on health? "))
        print(f" + {health} stamina  [bold red]{points_to_spend - health} [/bold red]points left")
        points_to_spend = points_to_spend - health
    
    
    
    
    Base_Character.update_attributes(stamina, attack, defense, health)
    return Base_Character



    print("╔═════════════════════╦════════════════╗")
    print("║          CHARACTER ATTRIBUTES        ║")
    print("╠═════════════════════╬════════════════╣")
    Base_Character.display_stats()
  




