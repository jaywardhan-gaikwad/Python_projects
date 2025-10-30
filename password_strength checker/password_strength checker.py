# ------------------------------------------
# PASSWORD STRENGTH CHECKER
# ------------------------------------------
# This program checks how strong a password is
# based on length, uppercase, lowercase, digits, and symbols.
# It shows a progress bar before displaying the result.
# ------------------------------------------

import re
from rich import print
from rich.progress import track
import time


# Function to check password strength
def check(password):
    score = 0
    missing = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        missing.append("Minimum 8 characters required.")

    # Lowercase check
    if re.search("[a-z]", password):
        score += 1
    else:
        missing.append("Add lowercase letters.")

    # Digit check
    if re.search("[0-9]", password):
        score += 1
    else:
        missing.append("Add digits.")

    # Uppercase check
    if re.search("[A-Z]", password):
        score += 1
    else:
        missing.append("Add uppercase letters.")

    # Special character check
    if re.search(r"[!@#$%^&*()_\-+={}\[\]:;\"'<>,.?/\\|]", password):
        score += 1
    else:
        missing.append("Add special symbols.")

    # Final evaluation
    if score == 5:
        print("\n[green]STRONG 💪[/green]")
    elif score >= 3:
        print("\n[yellow]MEDIUM 😐[/yellow]")
    else:
        print("\n[red]WEAK ⚠[/red]")

    # Display improvement suggestions
    if missing:
        print("[bold magenta]\nSUGGESTIONS:[/bold magenta]")
        for m in missing:
            print("-", m)


# Ask user for password input
password = input("ENTER PASSWORD: ")

# Simulate progress bar while checking
for step in track(range(10), description="[bold yellow]CHECKING STRENGTH OF PASSWORD...[/bold yellow]"):
    time.sleep(0.2)

# Call strength checking function
check(password)
