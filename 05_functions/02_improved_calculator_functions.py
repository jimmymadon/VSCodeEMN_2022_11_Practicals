def addition(pNumber1, pNumber2):
    return pNumber1 + pNumber2

def subtraction(pNumber1, pNumber2):
    return pNumber1 - pNumber2

def multiplication(pNumber1, pNumber2):
    return pNumber1 * pNumber2

def division(pNumber1, pNumber2):
    return round(pNumber1 / pNumber2, 2)

def isOptionValid(pMenuOption):
    if not pMenuOption.isnumeric():
        print("Please enter a valid digit!")
        return False

    pMenuOption = int(pMenuOption)
    if pMenuOption > 5 or pMenuOption < 1:
        print("Please enter a valid option!")
        return False

    return True

# Program begins from here
invalidAttempts = 0
while True:
    if invalidAttempts > 0:
        remainingAttempts = 3 - invalidAttempts
        print("You have", remainingAttempts, "attempts remaining!")

    if invalidAttempts == 3:
        print("Too many incorrect attempts! Quitting!")
        break

    print("""
    Menu:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Quit
    """)
    menuOption = input("Please enter a option between 1 and 4...\n")

    if not isOptionValid(menuOption):
        invalidAttempts = invalidAttempts + 1
        continue

    menuOption = int(menuOption)

    if menuOption == 5:
        break

    # Resetting invalidAttempts because option is valid at this point
    invalidAttempts = 0

    # Ask the user for 2 numbers and store them in 2 variables
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Display addition, subtraction, multiplication and division
    # of those 2 numbers
    if menuOption == 1:
        print("The sum of the 2 numbers is: ", addition(number1, number2))
    elif menuOption == 2:
        print("The difference of the 2 numbers is: ", subtraction(number1, number2))
    elif menuOption == 3:
        print("The product of the 2 numbers is: ", multiplication(number1, number2))
    else:
        print("The division value of the 2 numbers is: ", division(number1, number2))
