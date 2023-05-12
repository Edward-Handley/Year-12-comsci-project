import time
from rich import print
from Characters.Characters import Character,Enemy
from Game_Functions.Combat import Combat

def Intro():
   
    print("\n"
      "╔══════════════════════════════════════════╗\n"
      "║  Your journey will take you through      ║\n"
      "║  Freaky Forests, Terrifying Towns, and   ║\n"
      "║  Mysterious Marshlands. You will need to ║\n"
      "║  make smart decisions and have luck to   ║\n"
      "║  Win                                     ║\n"
      "╚══════════════════════════════════════════╝")


def Victory():#Victory function
    print("\n" * 2)
    print("[bold cyan]═════════════════════ VICTORY ═════════════════════[/bold cyan]")

    print("""
Congratulations, brave adventurer! You have successfully navigated through the Freaky Forrest, triumphed over the Terrifying Town, and conquered the Mysterious Marshland. You have proven your strength, courage, and resilience in the face of great danger.

As you stand victorious, the people from the nearby lands gather to celebrate your triumph. Tales of your heroism will be passed down through generations, and your name will be etched into the annals of history.

Your journey has come to an end, but your legend will live on forever.
    """)    




def Forrest(player):
    place_holder = "Freaky Forrest"
    print("\n" * 2)
    print(f"[bold green]{place_holder:^46}[/bold green]") 
    print("[bold green]" + "═" * 46 + "[/bold green]")
    #print("You start your journey in a descriptive on a narrow gravel path")
    print("""
You step into the lush, green forest, surrounded by the sounds of birds chirping and leaves rustling in the wind. The scent of damp earth and fresh vegetation fills the air. The sunlight filters through the canopy, casting dappled shadows on the forest floor. As you venture deeper into the woods, you can't help but feel a sense of adventure and danger lurking around every corner.
    """)
    run_or_walk = int(input("You see exit, run [1] or walk [2]"))
    if run_or_walk == 1:
        print("you begin to run for the exit, your footsteps crunch the gravel....")
        print("Just before you reach the exit a robber appears, you must fight him to get through")
        choice = "run"
    else:
        print("As you sneak past, you notice a movement in the bushes...")
        print("A robber appears, you must fight him to get through")
        choice = "walk"
    time.sleep(3)
    robber = Enemy("Robber", 80, 80, 80, 80)# Assigns enemy class vals to current enemy
    combat_result = Combat(player, robber)

    return choice, combat_result


def Town(player):
    place_holder = "Terrifying Town"
    print("\n" * 2)
    print(f"[bold blue]{place_holder:^46}[/bold blue]")
    print("[bold blue]" + "═" * 46 + "[/bold blue]")
    print("""
As you approach the Terrifying Town, you notice the cobblestone streets are eerily quiet. The once-bustling marketplace now lies abandoned, with stalls left in disarray. A cold wind blows through the desolate streets, carrying with it whispers of fear and uncertainty. Despite the unsettling atmosphere, you press on, determined to uncover the secrets hidden within this town.
    """)
    
    print("As you explore the town, you come across a rundown tavern.")
    action = int(input("Would you like to: \n1. Enter the tavern\n2. Continue exploring the town\nEnter your choice: "))
    
    if action == 1:
        print("You push open the creaky door of the tavern and step inside.")
        print("The tavern is dimly lit, with a few patrons huddled in a corner, nursing their drinks and murmuring amongst themselves.")
        print("Suddenly, a hooded figure approaches you, brandishing a dagger. It seems you've attracted some unwanted attention...")
        enemy = Enemy("Hooded Assassin", 90, 90, 90, 90)# Assigns enemy class vals to current enemy
    else:
        print("You decide to continue exploring the town, avoiding the ominous tavern.")
        print("As you round a corner, you find yourself face-to-face with a brutish-looking thug. He cracks his knuckles menacingly, demanding all of your belongings.")
        enemy = Enemy("Thug", 100, 80, 70, 90)# Assigns enemy class vals to current enemy
        
    combat_result = Combat(player, enemy)
    
    return "town", combat_result




def Marshland(player):
    place_holder = "Mysterious Marshland"
    print("\n" * 2)
    print(f"[bold magenta]{place_holder}[/bold magenta]")

    print("""
Entering the Mysterious Marshland, the air grows heavy with the scent of stagnant water and decay. The ground beneath your feet is soft and spongy, making every step a challenge. Strange noises echo through the foggy landscape, sending chills down your spine. You're determined to make it through this eerie place, but you know you must be on your guard.
    """)

    print("As you navigate the treacherous terrain, a swamp monster emerges from the murky waters, blocking your path.")
    print("You have no choice but to fight the swamp monster to continue your journey.")

    swamp_monster = Enemy("Swamp Monster", 100, 100, 100, 100) # Assigns enemy class vals to current enemy
    combat_result = Combat(player, swamp_monster)

    return "Marsh", combat_result

