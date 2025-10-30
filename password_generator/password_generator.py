# ------------------------------------------
# Password Generator
# ------------------------------------------
# This program generates a random password based on the length entered by the user.
# It uses symbols, numbers, and alphabets to create a strong password.
# The optional part (Rich library) can be used to add colorful progress bars and styled output.
# ------------------------------------------

import random
from rich.progress import track       # For showing a loading progress bar
from rich import print                # For colorful console output
import time                           # To add delay for visual effect

# Define character sets
symbols = '@!#~$%^&*'
numbers = '0123456789'
alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVWXYZ'

# Combine all characters into one string
all = symbols + numbers + alphabets

# Take password length input from user
length = int(input("Enter length for password: "))

# Generate the password randomly
password = ''.join(random.choices(all, k=length))

# Check for minimum length requirement
if length <= 4:
    print("[bold red]ATLEAST ENTER THE LENGTH ABOVE 5...[/bold red]")
else:
    # Show progress while generating password
    for step in track(range(10), description="[bold green]GENERATING PASSWORD...[/bold green]"):
        time.sleep(0.3)

    # Print the generated password
    print(f'[bold yellow]GENERATED PASSWORD:-[/bold yellow] [bold cyan]{password}[/bold cyan]')

# ------------------------------------------
# End of program
# ------------------------------------------
