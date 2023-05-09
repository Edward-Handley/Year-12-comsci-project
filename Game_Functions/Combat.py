
# import random
# from Characters.Characters import Character, Robber

# def Combat(player, enemy):
#     print("----------------------------------------------COMBAT-------------------------------------------- \n \n \n \n")
#     print(f"Combat between {player.name} and {enemy.name}")
#     turn = "p"
    
#     while player.health > 0 and enemy.health > 0:
#         if turn == "p":
#             P_move = int(input("Do you want to attack[1] or defend[2] \n Enter here: "))
#             if P_move == 1:
#                 P_attack_chance = (player.attack * random.uniform(0.8, 1.2)) / (enemy.defense * random.uniform(0.8, 1.2))
#                 if P_attack_chance > random.random():
#                     P_damage = max(1, int(player.attack * random.uniform(0.8, 1.2)))
#                     print(f"You hit {enemy.name} for {P_damage} damage")
#                     enemy.health -= P_damage
#                 else:
#                     print("You missed your attack")
#             elif P_move == 2:
#                 P_defense_chance = (player.defense * random.uniform(0.8, 1.2)) / (enemy.attack * random.uniform(0.8, 1.2))
#                 if P_defense_chance > random.random():
#                     print("You defend the enemies attack")
#                 else:
#                     E_damage = max(1, int(enemy.attack * random.uniform(0.8, 1.2)))
#                     print(f"You failed to defend their attack and took {E_damage} damage")
#                     player.health -= E_damage
#             turn = "e"
#         elif turn == "e":
#             print(f"Now it is {enemy.name}'s turn to attack")
#             E_attack_chance = (enemy.attack * random.uniform(0.8, 1.2)) / (player.defense * random.uniform(0.8, 1.2))
#             if E_attack_chance > random.random():
#                 E_damage = max(1, int(enemy.attack * random.uniform(0.8, 1.2)))
#                 print(f"{enemy.name} hit you for {E_damage} damage. You have {player.health - E_damage} health left")
#                 player.health -= E_damage
#             else:
#                 print(f"{enemy.name} missed their attack on you")
#             turn = "p"

#     if enemy.health <= 0:
#         print(f"You defeated {enemy.name}")
#         Combat_result = "win"
#     else:
#         print("You were defeated")
#         Combat_result = "lose"




###################################################OVER HAULD V2####################################################


# import random
# from Characters.Characters import Character, Robber

# def Combat(player, enemy):
#     print("----------------------------------------------COMBAT-------------------------------------------- \n \n \n \n")
#     print(f"Combat between {player.name} and {enemy.name}")

#     player_energy = 100
#     enemy_energy = 100

#     turn = "p"
    
#     while player.health > 0 and enemy.health > 0:
#         if turn == "p":
#             print(f"\nYour energy: {player_energy}")
#             print(f"Your health: {player.health}")
#             P_move = int(input("\nDo you want to:\n1. Normal attack\n2. Strong attack (costs 30 energy)\n3. Defend\n4. Strong defend (costs 30 energy)\nEnter your choice: "))

#             if player_energy < 30 and (P_move == 2 or P_move == 4):
#                 print("Not enough energy for this action!")
#                 continue

#             if P_move == 1 or P_move == 2:
#                 P_attack = player.attack * (1.5 if P_move == 2 else 1)
#                 P_attack_chance = (P_attack * random.uniform(0.8, 1.2)) / (enemy.defense * random.uniform(0.8, 1.2))
#                 critical_hit = random.random() < 0.1

#                 if P_attack_chance > random.random():
#                     P_damage = max(1, int(P_attack * random.uniform(0.8, 1.2))) * (2 if critical_hit else 1)
#                     print(f"\nYou hit {enemy.name} for {P_damage} damage" + (" (CRITICAL HIT!)" if critical_hit else ""))
#                     enemy.health -= P_damage
#                 else:
#                     print("\nYou missed your attack")

#                 if P_move == 2:
#                     player_energy -= 30

#             elif P_move == 3 or P_move == 4:
#                 player.defense *= 1.5 if P_move == 4 else 1
#                 P_defense_chance = (player.defense * random.uniform(0.8, 1.2)) / (enemy.attack * random.uniform(0.8, 1.2))
                
#                 if P_defense_chance > random.random():
#                     print("\nYou brace yourself for the enemy's attack")
#                 else:
#                     E_damage = max(1, int(enemy.attack * random.uniform(0.8, 1.2)))
#                     print(f"\nYou failed to defend their attack and took {E_damage} damage")
#                     player.health -= E_damage

#                 if P_move == 4:
#                     player_energy -= 30

#             else:
#                 print("Invalid input. Please enter a number between 1 and 4.")
#                 continue

#             turn = "e"
#             player_energy = min(player_energy + 10, 100)

#         elif turn == "e":
#             print(f"\nNow it is {enemy.name}'s turn to attack")

#             enemy_choice = random.choices([1, 2, 3, 4], weights=[40, 20, 30, 10], k=1)[0]

#             if enemy_energy < 30 and (enemy_choice == 2 or enemy_choice == 4):
#                 enemy_choice = 1 if enemy_choice == 2 else 3

#             if enemy_choice == 1 or enemy_choice == 2:
#                 E_attack = enemy.attack * (1.5 if enemy_choice == 2 else 1)
#                 E_attack_chance = (E_attack * random.uniform(0.8, 1.2)) / (player.defense * random.uniform(0.8, 1.2))
#                 critical_hit = random.random() < 0.1

#             if E_attack_chance > random.random():
#                 E_damage = max(1, int(E_attack * random.uniform(0.8, 1.2))) * (2 if critical_hit else 1)
#                 print(f"{enemy.name} hit you for {E_damage} damage" + (" (CRITICAL HIT!)" if critical_hit else "") + f". You have {player.health - E_damage} health left")
#                 player.health -= E_damage
#             else:
#                 print(f"{enemy.name} missed their attack on you")

#             if enemy_choice == 2:
#                 enemy_energy -= 30

#         elif enemy_choice == 3 or enemy_choice == 4:
#             enemy.defense *= 1.5 if enemy_choice == 4 else 1
#             E_defense_chance = (enemy.defense * random.uniform(0.8, 1.2)) / (player.attack * random.uniform(0.8, 1.2))

#             if E_defense_chance > random.random():
#                 print(f"{enemy.name} braces for your attack")
#             else:
#                 P_damage = max(1, int(player.attack * random.uniform(0.8, 1.2)))
#                 print(f"\nYou hit {enemy.name} for {P_damage} damage")
#                 enemy.health -= P_damage

#             if enemy_choice == 4:
#                 enemy_energy -= 30

#         turn = "p"
#         enemy_energy = min(enemy_energy + 10, 100)

#     if enemy.health <= 0:
#         print(f"\nYou defeated {enemy.name}")
#         Combat_result = "win"
#     else:
#         print("\nYou were defeated")
#         Combat_result = "lose"



############################################OVERHAULED V2.1###########################################
import random
from rich import print
from Characters.Characters import Character, Robber

def Combat(player, enemy):
    print("----------------------------------------------[bold red]COMBAT[/bold red]--------------------------------------------\n")
    print(f"Combat between [bold]{player.name}[/bold] and [bold]{enemy.name}[/bold]\n")

    player_energy = 100
    enemy_energy = 100

    turn = "p"

    while player.health > 0 and enemy.health > 0:
        if turn == "p":
            print(f"\nYour energy: [bold green]{player_energy}[/bold green]")
            print(f"Your health: [bold green]{player.health}[/bold green]")
            P_move = int(input("\nDo you want to:\n1. Normal attack\n2. Strong attack (costs 30 energy)\n3. Defend\n4. Strong defend (costs 30 energy)\nEnter your choice: "))

            if player_energy < 30 and (P_move == 2 or P_move == 4):
                print("[red]Not enough energy for this action![/red]")
                continue

            if P_move == 1 or P_move == 2:
                P_attack = player.attack * (1.5 if P_move == 2 else 1)
                P_attack_chance = (P_attack * random.uniform(0.8, 1.2)) / (enemy.defense * random.uniform(0.8, 1.2))
                critical_hit = random.random() < 0.1

                if P_attack_chance > random.random():
                    P_damage = max(1, int(P_attack * random.uniform(0.8, 1.2))) * (2 if critical_hit else 1)
                    print(f"\nYou hit [bold]{enemy.name}[/bold] for [bold]{P_damage}[/bold] damage" + (" [bold red](CRITICAL HIT!)[/bold red]" if critical_hit else ""))
                    enemy.health -= P_damage
                else:
                    print("\n[red]You missed your attack[/red]")

                if P_move == 2:
                    player_energy -= 30

            elif P_move == 3 or P_move == 4:
                player.defense *= 1.5 if P_move == 4 else 1

                turn = "e"
                player_energy = min(player_energy + 10, 100)

        elif turn == "e":
            print(f"\nNow it is [bold]{enemy.name}[/bold]'s turn to attack")

            enemy_choice = random.choices([1, 2, 3, 4], weights=[40, 20, 30, 10], k=1)[0]

            if enemy_energy < 30 and (enemy_choice == 2 or enemy_choice == 4):
                enemy_choice = 1 if enemy_choice == 2 else 3

            if enemy_choice == 1 or enemy_choice == 2:
                E_attack = enemy.attack * (1.5 if enemy_choice == 2 else 1)
                E_attack_chance = (E_attack * random.uniform(0.8, 1.2)) / (player.defense * random.uniform(0.8, 1.2))
                critical_hit = random.random() < 0.1

                if E_attack_chance > random.random():
                                    E_damage = max(1, int(E_attack * random.uniform(0.8, 1.2))) * (2 if critical_hit else 1)
                print(f"{enemy.name} hit you for [bold]{E_damage}[/bold] damage" + (" [bold red](CRITICAL HIT!)[/bold red]" if critical_hit else "") + f". You have [bold green]{player.health - E_damage}[/bold green] health left")
                player.health -= E_damage
            else:
                print(f"{enemy.name} missed their attack on you")

            if enemy_choice == 2:
                enemy_energy -= 30

        elif enemy_choice == 3 or enemy_choice == 4:
            enemy.defense *= 1.5 if enemy_choice == 4 else 1
            E_defense_chance = (enemy.defense * random.uniform(0.8, 1.2)) / (player.attack * random.uniform(0.8, 1.2))

            if E_defense_chance > random.random():
                print(f"{enemy.name} braces for your attack")
            else:
                P_damage = max(1, int(player.attack * random.uniform(0.8, 1.2)))
                print(f"\nYou hit {enemy.name} for [bold]{P_damage}[/bold] damage")
                enemy.health -= P_damage

            if enemy_choice == 4:
                enemy_energy -= 30

        turn = "p"
        enemy_energy = min(enemy_energy + 10, 100)

    if enemy.health <= 0:
        print(f"\nYou defeated [bold]{enemy.name}[/bold]")
        Combat_result = "win"
    else:
        print("\n[red]You were defeated[/red]")
        Combat_result = "lose"


