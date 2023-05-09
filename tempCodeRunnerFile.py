def main():
    
    Pcharacter = Create_Character()
    
    want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
    while want_Intro != "Y" and want_Intro != "N":
        print("Invalid entry try again")
        want_Intro = input("Do you want an intro to the game?   [Y/N]").upper()
    if want_Intro == "Y":
        Intro()
    else:
        print("No intro, Good luck!")
    



    print(f"Your character is Knight{Pcharacter.name} game will now begin....... good luck ")
  
  
    forrest_result, combat_result = Forrest(Pcharacter)
    #Combat Result returning "None" need to fix this 
   



    #Combat(Pcharacter, enemy)

main()