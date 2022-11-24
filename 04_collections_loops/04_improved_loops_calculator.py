print("""
Menu:
1. Addition
2. Subtraction
3. Multiplication
4. Division
""")
menuOption = input("Please enter a option between 1 and 4...\n")

if not menuOption.isnumeric():
    print("Please enter a valid digit!")
    exit()

menuOption = int(menuOption)

if menuOption > 4 or menuOption < 1:
    print("Please enter a valid option!")
    exit()

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
