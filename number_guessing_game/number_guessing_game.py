# ------------------------------------------
# NUMBER GUESSING GAME
# ------------------------------------------
# The program randomly selects a number between 1 and 20.
# The player has 5 chances to guess the correct number.
# After each wrong guess, the program gives a hint.
# ------------------------------------------

import random
from rich import print

# Generate a random number between 1 and 20
number = random.randint(1, 20)
chances = 5

print("[bold magenta]---- LET'S PLAY ----[/bold magenta]")
print("[bold magenta]NUMBER IS BETWEEN 1 - 20[/bold magenta]")

# Game loop (runs while player still has chances)
while chances > 0:
    guess = int(input("\nGUESS THE NUMBER: "))

    if guess == number:
        print("[bold green]YOU GUESSED IT RIGHT! 🎉[/bold green]")
        break
    else:
        # Give a hint to the player
        if number > guess:
            print(f"[bold white]NUMBER IS ABOVE {guess}.[/bold white]")
        else:
            print(f"[bold white]NUMBER IS BELOW {guess}.[/bold white]")

        # Reduce chances after each wrong guess
        chances -= 1
        print(f"CHANCES LEFT = [bold yellow]{chances}[/bold yellow]")
        print("[bold red]TRY AGAIN 😅!![/bold red]")

# When no chances left
if chances == 0:
    print(f"[bold red]\nOut of chances! The number was {number}.[/bold red]")

print("[bold blue]\n--- THANK YOU FOR PLAYING ---[/bold blue]")
