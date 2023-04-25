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


def Intro():
    print("You are a brave knight who is trying to return home from an epic battle")
    print("You have been travelling for days and are now in a forest \n you must play to your strengths to defeat enemies in three different areas")
    print("The frightening forest")
    print("The hostile vilage")
    print("The trecherous marsh lands")
    print("Once you do all these you can return home to your kingdom")
    print("Good luck")





def main():
    print("Welcome to .... game")
    print("First you have to make your character")
    #start = input("Read to start [Y/N]")
    #if start != "Y" or "N":
    #   print("Invalid entry please try again")
    #   start = input("Read to start [Y/N]")
    name = input("What shall your knight be called? ")
    Knight = Character(name, 80,80,80,80,)
    print(f"Knight {name}, wonderfull name")
    print("Here are your current stats")
    print(f"Stamina: {Knight.stamina}")
    print(f"Attack: {Knight.attack}")
    print(f"Defense: {Knight.defense}")
    print(f"Health: {Knight.health}")
    print("Now you can choose to upgrade your stats")
    print("You can upgrade your stats by 20 points to a max of 100, however you have to share the 20 points between all stats")
    points_to_spend = 20

    while points_to_spend > 0:
        print(f"You have {points_to_spend} points to spend")
        stamina = int(input("How many points would you like to spend on Stamina?"))
        while stamina > points_to_spend:
            print("You don't have enough points to spend")
            stamina = int(input("How many points would you like to spend on Stamina?"))

        attack = int(input("How many points would you like to spend on Attack?"))
        while attack > points_to_spend:
            print("You don't have enough points to spend")
            attack = int(input("How many points would you like to spend on Attack?"))

        defense = int(input("How many points would you like to spend on Defense?"))
        while defense > points_to_spend:
            print("You don't have enough points to spend")
            defense = int(input("How many points would you like to spend on Defense?"))

        health = int(input("How many points would you like to spend on Health?"))
        while health > points_to_spend:
            print("You don't have enough points to spend")
            health = int(input("How many points would you like to spend on Health?"))

        points_to_spend -= (stamina + attack + defense + health)

        if points_to_spend < 0:
            print("You have spent too many points, please try again")
            points_to_spend = 20
        else:
            print("You have spent all your points")
            Knight.update_attributes(stamina, attack, defense, health)
            
            #print("Here are your new stats")
            #
            # Knight.display_stats()
#Prints the character stats in a table
    print("╔════════════════════════════╦════════════════╗")
    print("║         CHARACTER ATTRIBUTES        ║                ║")
    print("╠════════════════════════════╬════════════════╣")
    Knight.display_stats()

        
        
    print("""\
              ______________                               
                        ,===:'.,            `-._                           
            `:.     `--.         `.                     
                                 \.        `.         `.                   
                         (,,(,    \.         `.   ____,-`.,                
                      (,'     `/   \.   ,--.___`.'                         
                  ,  ,'  ,--.  `,   \.;'         `                         
                   `{D, {    \  :    \;                                    
                     V,,'    /  /    //                                    
                     j;;    /  ,' ,-//.    ,---.      ,                    
                     \;'   /  ,' /  _  \  /  _  \   ,'/                    
                           \   `'  / \  `'  / \  `.' /                     
                            `.___,'   `.__,'   `.__,' 
        
        """)
    print("\n \n \n")
    intro = input("Do you want an intro to the game? [Y/N]")
    while intro not in ["Y", "N"]:
        print("Invalid entry, please try again")
        intro = input("Do you want an intro to the game? [Y/N]")

    if intro == "Y":
        Intro()
    else:
        print("Good luck")
        

main()