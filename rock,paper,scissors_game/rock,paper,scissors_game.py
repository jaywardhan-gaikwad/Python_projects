# ------------------------------------------
# ROCK, PAPER, SCISSORS GAME
# ------------------------------------------
# The player competes with the computer in 3 rounds.
# Whoever wins 2 or more rounds first wins the match.
# Emojis are kept for fun 😎
# ------------------------------------------

import random
from rich import print

game = ['rock', 'paper', 'scissors']
print("[bold black]--- LET'S PLAY ---[/bold black]")

user_win = 0
computer_win = 0
tie = 0
rounds = 3  # Total number of rounds

while rounds > 0:
    user = input("Enter Rock, Paper, or Scissors: ").lower()
    ran = random.choice(game)  # computer's choice for each round

    if user not in game:
        print("[bold red]ENTER VALID CHOICE!!![/bold red]")
        continue

    # WIN condition for user
    if (user == 'rock' and ran == 'scissors') or \
       (user == 'paper' and ran == 'rock') or \
       (user == 'scissors' and ran == 'paper'):
        print('[bold green]YOU WON 😒[/bold green]')
        print(f"[bold white]I CHOSE {ran}[/bold white]")
        user_win += 1

    # TIE condition
    elif user == ran:
        print("[bold red]IT WAS A TIE..[/bold red]")
        print(f"[bold white]I CHOSE {ran}[/bold white]")
        tie += 1
        if tie >= 2:
            rounds += 1
            print("\nONE MORE MATCH TO DECIDE THE WINNER!")
            continue

    # WIN condition for computer
    else:
        print('[bold yellow]I WON 😎[/bold yellow]')
        print(f"[bold white]I CHOSE {ran}[/bold white]")
        computer_win += 1

    rounds -= 1  # Decrease remaining rounds after each valid play

# FINAL RESULT
print("\n------------------------------------------")
if user_win > computer_win:
    print("\n[bold cyan]YOU WON THE GAME...[/bold cyan]")
    print(f"[bold blue]YOU WON {user_win} ROUND(S).[/bold blue]")
elif computer_win > user_win:
    print("\n[bold cyan]I WON THE GAME....[/bold cyan]")
    print(f"[bold blue]I WON {computer_win} ROUND(S).[/bold blue]")
else:
    print("\n[bold cyan]GAME ENDED IN A TIE![/bold cyan]")
print("[bold magenta]IT WAS NICE PLAYING WITH YOU.... 😊[/bold magenta]")
print("[bold magenta]THANK YOU![/bold magenta]")
