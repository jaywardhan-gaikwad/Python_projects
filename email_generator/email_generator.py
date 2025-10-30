# ------------------------------------------
# EMAIL GENERATOR
# ------------------------------------------
# This program automatically generates multiple unique email
# suggestions based on the user's full name.
# It adds random numbers and combines first and last names
# in different patterns to create variations.
# ------------------------------------------

import random
from rich.progress import track
from rich import print
import time

# Ask user for full name and clean it
name = input("Enter full name: ").strip().lower()

# Generate 5 random numbers between 1 and 999
ran = random.choices(range(1, 1000), k=5)

# Split name into parts
name_parts = name.split()
first = name_parts[0]
last = name_parts[-1] if len(name_parts) > 1 else ''

# Domain for email generation,the domain is only for google mail
# u can add other mails domain as per ur need like yahoo,outlook etc.
domains = "gmail.com"

# Empty list to store generated email patterns
emails = []

# Different styles of email combinations
emails.append(f"{first}{last}{ran[0]}@{domains}")
emails.append(f"{last}{first}{ran[1]}@{domains}")
emails.append(f"{first}{last}@{domains}")
emails.append(f"{last}{first}@{domains}")
emails.append(f"{last}{ran[2]}{first}@{domains}")
emails.append(f"{ran[3]}{first}{last}@{domains}")
emails.append(f"{first}{ran[4]}@{domains}")

# Show progress bar while generating
for step in track(range(10), description="[bold green]GENERATING EMAILS...[/bold green]"):
    time.sleep(0.2)

# Display generated emails
print("\n[bold cyan]GENERATED EMAILS:[/bold cyan]")
for e in emails:
    print(f"[bold magenta]{e}[/bold magenta]")

print("\n[bold blue]--- THANK YOU FOR USING EMAIL GENERATOR ---[/bold blue]")
