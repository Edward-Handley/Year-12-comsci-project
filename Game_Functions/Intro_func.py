import random

from Characters.Characters import Character, Robber
from Game_Functions.Combat import Combat


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
