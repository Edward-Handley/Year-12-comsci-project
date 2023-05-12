import random
import rich as print
import time

from Characters.Characters import *
from Game_Functions.Intro_func import *

try:
    import rich
except ImportError:
    print("The 'rich library is required to play this game")
    print("install it using the command \n")
    print("pip install rich")


def main():
    print("[bold blue]Welcome to the game![/bold blue]")
    Pcharacter = Create_Character()

    want_Intro = input("Do you want an intro to the game? [Y/N] ").upper() # Does user want an intro?
    while want_Intro != "Y" and want_Intro != "N":
        print("Invalid entry try again")
        want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
    if want_Intro == "Y":#Runs intro function
        Intro()
        time.sleep(3)
    else:
        print("No intro, Good luck!")

    
    print(f"Your character is Knight[bold blue] {Pcharacter.name} [/bold blue] game will now begin....... good luck ")

    #Starts the Scenarios
    forrest_result, combat_result = Forrest(Pcharacter)
    time.sleep(3)  # Pause for 3 seconds
    

    town_result = Town(Pcharacter)
    time.sleep(3)  # Pause for 3 seconds

    marshland_result = Marshland(Pcharacter)
    print(marshland_result)

    if marshland_result == "win":
        time.sleep(3)  # Pause for 3 seconds
        Victory() # Runs Victory Function

#main()

if __name__ == "__main__":
    main()
