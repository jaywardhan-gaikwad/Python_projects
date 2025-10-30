# ------------------------------------------
# Age Calculator
# ------------------------------------------
# This program calculates your exact age in years, months, and days
# based on your date of birth entered in the format YYYY-MM-DD.
# It uses the datetime and dateutil modules for accurate date handling.
# ------------------------------------------

from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from rich import print  # For colorful and styled output in the terminal

# Ask the user to enter their birthdate
dob = input("ENTER YOUR BIRTHDATE (YYYY-MM-DD): ")

# Convert the input string into a date object
birth_date = datetime.strptime(dob, "%Y-%m-%d").date()

# Get today's date
today = date.today()

# Calculate the difference between today's date and birth date
age = relativedelta(today, birth_date)

# Display the age in years, months, and days
print(f'\n[bold white]You are {age.years} years, {age.months} months, and {age.days} days old.[/bold white]')

# ------------------------------------------
# End of program
# ------------------------------------------
