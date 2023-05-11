import random
import rich
import time
import json
from Characters.Characters import *
from Game_Functions.Intro_func import *



def save_game(player):
    save_data = {
        "name": player.name,
        "stamina": player.stamina,
        "attack": player.attack,
        "defense": player.defense,
        "health": player.health,
        "inventory": player.inventory  # Save inventory
    }
    with open("save_game.json", "w") as save_file:
        json.dump(save_data, save_file)
    print("Game saved successfully!")

def load_game():
    with open("save_game.json", "r") as save_file:
        save_data = json.load(save_file)
    loaded_player = Character(
        save_data["name"],
        save_data["stamina"],
        save_data["attack"],
        save_data["defense"],
        save_data["health"]
    )
    loaded_player.inventory = save_data["inventory"]  # Load inventory
    print("Game loaded successfully!")
    return loaded_player


# def main():

#     Pcharacter = Create_Character()

#     want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
#     while want_Intro != "Y" and want_Intro != "N":
#         print("Invalid entry try again")
#         want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
#     if want_Intro == "Y":
#         Intro()
#     else:
#         print("No intro, Good luck!")

    
#     print(f"Your character is Knight[bold blue] {Pcharacter.name} [/bold blue] game will now begin....... good luck ")

#     forrest_result, combat_result = Forrest(Pcharacter)
#     time.sleep(3)  # Pause for 3 seconds
    

#     town_result = Town(Pcharacter)
#     time.sleep(3)  # Pause for 3 seconds

#     marshland_result = Marshland(Pcharacter)

#     if marshland_result == "win":
#         time.sleep(3)  # Pause for 3 seconds
#         Victory()

# main()

def main():
    print("Welcome to the game!")
    print("1. New Game")
    print("2. Load Game")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        Pcharacter = Create_Character()
    elif choice == "2":
        Pcharacter = load_game()
    else:
        print("Invalid choice. Exiting the game.")
        return

    want_Intro = input("Do you want an intro to the game? [Y/N] ").upper()
    # ... (rest of the main function)
    while want_Intro != "Y" and want_Intro != "N":
        print("Invalid entry try again")
        want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
    if want_Intro == "Y":
        Intro()
    else:
        print("No intro, Good luck!")

    
    print(f"Your character is Knight[bold blue] {Pcharacter.name} [/bold blue] game will now begin....... good luck ")

    forrest_result, combat_result = Forrest(Pcharacter)
    time.sleep(3)  # Pause for 3 seconds
    

    town_result = Town(Pcharacter)
    time.sleep(3)  # Pause for 3 seconds

    marshland_result = Marshland(Pcharacter)

    if marshland_result == "win":
        time.sleep(3)  # Pause for 3 seconds
        Victory()


    # After completing the game, prompt the user to save their progress
    save_choice = input("Do you want to save your progress? [Y/N] ").upper()
    if save_choice == "Y":
        save_game(Pcharacter)
        print("Your progress has been saved.")

main()
