# ------------------------------------------
# SIMPLE CALCULATOR
# ------------------------------------------
# Performs multiple arithmetic operations such as:
# addition, subtraction, multiplication, division,
# floor division, modulus, and exponentiation.
# The program allows the user to select operations repeatedly.
# ------------------------------------------

# Function to add numbers
def add_numbers():
    total = 0
    count = int(input("HOW MANY NUMBERS DO YOU WANT TO ADD: "))
    for i in range(count):
        num = float(input(f"ENTER NUMBER {i + 1}: "))
        total += num
    print("SUM =", total)


# Function to subtract numbers
def sub_numbers():
    count = int(input("HOW MANY NUMBERS DO YOU WANT TO SUBTRACT: "))
    first = float(input("ENTER NUMBER 1: "))
    result = first
    for i in range(count - 1):
        num = float(input(f"ENTER NUMBER {i + 2}: "))
        result -= num
    print("RESULT =", result)


# Function to multiply numbers
def multiply_numbers():
    result = 1
    count = int(input("HOW MANY NUMBERS DO YOU WANT TO MULTIPLY: "))
    for i in range(count):
        num = float(input(f"ENTER NUMBER {i + 1}: "))
        result *= num
    print("PRODUCT =", result)


# Function to divide numbers
def division_numbers():
    count = int(input("HOW MANY NUMBERS DO YOU WANT TO DIVIDE: "))
    first = float(input("ENTER NUMBER 1: "))
    result = first
    for i in range(count - 1):
        num = float(input(f"ENTER NUMBER {i + 2}: "))
        if num == 0:
            print("ERROR: DIVISION BY ZERO!!")
            return
        result /= num
    print("RESULT =", result)


# Function to perform floor division
def floordivide_numbers():
    count = int(input("HOW MANY NUMBERS DO YOU WANT TO FLOOR DIVIDE: "))
    first = float(input("ENTER NUMBER 1: "))
    result = first
    for i in range(count - 1):
        num = float(input(f"ENTER NUMBER {i + 2}: "))
        if num == 0:
            print("ERROR: DIVISION BY ZERO!!")
            return
        result //= num
    print("RESULT =", result)


# Function to find modulus
def modulus():
    a = float(input("ENTER NUMBER 1: "))
    b = float(input("ENTER NUMBER 2: "))
    if b == 0:
        print("ERROR: DIVISION BY ZERO!!")
    else:
        print("REMAINDER =", a % b)


# Function for exponentiation
def exponentiation():
    a = float(input("ENTER BASE: "))
    b = float(input("ENTER EXPONENT: "))
    print("RESULT =", a ** b)


# ------------------------------------------
# Main program loop
# ------------------------------------------
while True:
    print("\n--- SIMPLE CALCULATOR ---")
    print("\nOPTIONS FOR OPERATIONS:")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. FLOOR DIVISION")
    print("6. MODULUS")
    print("7. EXPONENTIATION")
    print("8. EXIT")

    # Taking user choice
    choice = int(input("ENTER CHOICE (1-8): "))

    # Performing selected operation
    if choice == 1:
        add_numbers()
    elif choice == 2:
        sub_numbers()
    elif choice == 3:
        multiply_numbers()
    elif choice == 4:
        division_numbers()
    elif choice == 5:
        floordivide_numbers()
    elif choice == 6:
        modulus()
    elif choice == 7:
        exponentiation()
    elif choice == 8:
        print("EXITING...")
        break
    else:
        print("INVALID CHOICE!!")

# ------------------------------------------
# End of program
# ------------------------------------------
