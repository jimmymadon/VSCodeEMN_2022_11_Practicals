# Show the menu to user and continue the program until the user
# enters option number 5

# Now we put the WHOLE program inside the infinite while loop
# And we will break ONLY when the option == 5
while True:
    print("""
    Menu:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Quit
    """)
    menuOption = input("Please enter a option between 1 and 4...\n")

    if not menuOption.isnumeric():
        print("Please enter a valid digit!")
        invalidAttempts = invalidAttempts + 1
        continue

    menuOption = int(menuOption)

    if menuOption > 5 or menuOption < 1:
        print("Please enter a valid option!")
        invalidAttempts = invalidAttempts + 1
        continue

    if menuOption == 5:
        break # Come out of the loop when option is 5

    # Ask the user for 2 numbers and store them in 2 variables
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Display addition, subtraction, multiplication and division
    # of those 2 numbers
    if menuOption == 1:
        print("The sum of the 2 numbers is: ", number1 + number2)
    elif menuOption == 2:
        print("The difference of the 2 numbers is: ", number1 - number2)
    elif menuOption == 3:
        print("The product of the 2 numbers is: ", number1 * number2)
    else:
        print("The division value of the 2 numbers is: ", round(number1 / number2, 2))
