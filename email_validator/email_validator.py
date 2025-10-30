# ------------------------------------------
# Email Validator
# ------------------------------------------
# This program checks if an entered email address is valid
# by verifying lowercase characters, presence of '@', and domain structure.
# It helps users quickly test whether their email follows proper format rules.
# ------------------------------------------

from rich import print  # For colorful styled output

# Take email input from user
email = input("Enter an email: ").strip()

# List to store validation issues
problems = []

# Check if email contains only lowercase letters
if not email.islower():
    problems.append("[red]Email must be in lowercase.[/red]")

# Check if email contains spaces
if " " in email:
    problems.append("[red]Email must not contain spaces.[/red]")

# Check if '@' symbol exists
if "@" not in email:
    problems.append("[red]Email must contain '@' symbol.[/red]")
else:
    # Split email into two parts: local part and domain
    local, domain = email.split("@", 1)
    
    # Check if domain contains a dot '.'
    if "." not in domain:
        problems.append("[red]Email must have a domain (e.g., gmail.com).[/red]")

# Final output
if problems:
    print("\n[bold yellow]Invalid Email! Problems found:[/bold yellow]")
    for issue in problems:
        print("-", issue)
else:
    print("\n[bold green]Valid Email Address![/bold green]")

# ------------------------------------------
# End of program
# ------------------------------------------
