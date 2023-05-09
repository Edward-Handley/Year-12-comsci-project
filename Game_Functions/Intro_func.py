import random
from rich import print
from Characters.Characters import Character, Robber
from Game_Functions.Combat import Combat

def section_Headings(place_holder):
    print("\n" * 2)
    print(f"[bold green]{place_holder:^46}[/bold green]")
    print("[bold green]" + "═" * 46 + "[/bold green]")




def Intro():
   
    print("\n"
      "╔══════════════════════════════════════════╗\n"
      "║  Your journey will take you through      ║\n"
      "║  Freaky Forests, Terrifying Towns, and   ║\n"
      "║  Mysterious Marshlands. You will need to ║\n"
      "║  make smart decisions and have luck to   ║\n"
      "║  Win                                     ║\n"
      "╚══════════════════════════════════════════╝")





def Forrest(player):
    place_holder = "Freaky Forrest"
    # print("\n"
    #   "╔══════════════════════════════════════════╗\n"
    #   "║            The Freaky Forest             ║\n"
    #   "║                                          ║\n"
    # )
    print("\n" * 2)
    print(f"[bold green]{place_holder:^46}[/bold green]")
    print("[bold green]" + "═" * 46 + "[/bold green]")
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


def Town(player):
    place_holder = "Terrifying Town"
    print("\n" * 2)
    section_Headings(place_holder)
