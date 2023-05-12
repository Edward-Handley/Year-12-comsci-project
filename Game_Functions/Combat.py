
import random
from rich import print
from Characters.Characters import Character, Enemy

def Combat(player, enemy):
    print("----------------------------------------------[bold red]COMBAT[/bold red]--------------------------------------------\n")
    print(f"Combat between [bold]{player.name}[/bold] and [bold]{enemy.name}[/bold]\n")
    print(f"Enemy stats: [bold]{enemy.stamina}[/bold] stamina, [bold]{enemy.attack}[/bold] attack, [bold]{enemy.defense}[/bold] defense, [bold]{enemy.health}[/bold] health\n")

    player_energy = 100 # Sets player and enemy energy
    enemy_energy = 100

    turn = "p" # Assigns the turn to player by default

    while player.health > 0 and enemy.health > 0:
        if turn == "p":
            print(enemy.health )#debug
            print(f"\nYour energy: [bold green]{player_energy}[/bold green]")
            print(f"Your health: [bold green]{player.health}[/bold green]")
            P_move = int(input("\nDo you want to:\n1. Normal attack\n2. Strong attack (costs 30 energy)\n3. Defend\n4. Strong defend (costs 30 energy)\nEnter your choice: "))

            if player_energy < 30 and (P_move == 2 or P_move == 4):
                print("[red]Not enough energy for this action![/red]")
                continue

            if P_move == 1 or P_move == 2: #Handles the Player Attack moves
                P_attack = player.attack * (1.5 if P_move == 2 else 1)
                P_attack_chance = (P_attack * random.uniform(0.8, 1.2)) / (enemy.defense * random.uniform(0.8, 1.2)) # Generates a random number between 0.8 and 1.2 and multiplies it by the attack and defense values to simulate a random chance of hitting credit:https://chat.openai.com/
                critical_hit = random.random() < 0.1

                if P_attack_chance > random.random(): # If the attack chance is greater than a random number between 0 and 1, the attack hits
                    P_damage = max(1, int(P_attack * random.uniform(0.8, 1.2))) * (2 if critical_hit else 1)
                    print(f"\nYou hit [bold]{enemy.name}[/bold] for [bold]{P_damage}[/bold] damage" + (" [bold red](CRITICAL HIT!)[/bold red]" if critical_hit else ""))
                    enemy.health -= P_damage
                else:
                    print("\n[red]You missed your attack[/red]")

                if P_move == 2: #Subtracts energy for power hit
                    player_energy -= 30

            elif P_move == 3 or P_move == 4: #Handles Defenseive moves
                player.defense *= 1.5 if P_move == 4 else 1
                if P_move == 4:
                    player_energy -= 30
                
                turn = "e" # If Defense move = True then turn = enemy
            player_energy = min(player_energy + 10, 100) #Replenishes Energy

        elif turn == "e": #Handles the Enemy's turn
            print(f"\nNow it is [bold]{enemy.name}[/bold]'s turn to attack")

            enemy_choice = random.choices([1, 2, 3, 4], weights=[40, 20, 30, 10], k=1)[0] #Enemy choice is random credit:https://chat.openai.com/

            if enemy_energy < 30 and (enemy_choice == 2 or enemy_choice == 4): #Handles if choice requires energy but enemy has insufficient
                enemy_choice = 1 if enemy_choice == 2 else 3

            if enemy_choice == 1 or enemy_choice == 2:
                E_attack = enemy.attack * (1.5 if enemy_choice == 2 else 1)
                E_attack_chance = (E_attack * random.uniform(0.8, 1.2)) / (player.defense * random.uniform(0.8, 1.2))
                critical_hit = random.random() < 0.1

                if E_attack_chance > random.random():
                    E_damage = max(1, int(E_attack * random.uniform(0.8, 1.2))) * (2 if critical_hit else 1)#https://chat.openai.com/
                    print(f"{enemy.name} hit you for [bold]{E_damage}[/bold] damage" + (" [bold red](CRITICAL HIT!)[/bold red]" if critical_hit else "") + f". You have [bold green]{player.health - E_damage}[/bold green] health left")
                    player.health -= E_damage
                else:
                    print(f"{enemy.name} missed their attack on you")

                if enemy_choice == 2:
                    enemy_energy -= 30

            elif enemy_choice == 3 or enemy_choice == 4:
                enemy.defense *= 1.5 if enemy_choice == 4 else 1

            turn = "p" # Returns the turn to the player
            enemy_energy = min(enemy_energy + 10, 100) 

    if enemy.health <= 0:
        print(f"\nYou defeated [bold]{enemy.name}[/bold]")
        Combat_result = "win"
    else:
        print("\n[red]You were defeated[/red]")
        Combat_result = "lose"

    return Combat_result
