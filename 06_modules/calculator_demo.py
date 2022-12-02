import operations

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

    if not operations.isOptionValid(menuOption):
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
        print("The sum of the 2 numbers is: ", operations.addition(number1, number2))
    elif menuOption == 2:
        print("The difference of the 2 numbers is: ", operations.subtraction(number1, number2))
    elif menuOption == 3:
        print("The product of the 2 numbers is: ", operations.multiplication(number1, number2))
    else:
        print("The division value of the 2 numbers is: ", operations.division(number1, number2))
