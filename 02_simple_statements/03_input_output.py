print("Hello World")
print(10)
print(True)

welcomeMessage = "Welcome Jimmy!"
print(welcomeMessage)

# Addition (Concatenation or joining) of strings
userName = "Jimmy"
print(userName)
welcomeMessage2 = "Hello " + userName + "!"
print(welcomeMessage2)

# Two ways of printing multiple pieces of data
firstName = "Jimmy"
lastName = "Madon"
print("Hello " + firstName + " " + lastName) # print is displaying ONE combined string
print("Hello", firstName, lastName + "!") # print is displaying THREE strings
print("The value of a number is: ", 10) # print converts 10 to str and then combines and displays
print("The value of a number is: " + "10")

# Asking for user's input (input always gives you a str)
name = input("What is your name?\n")
print("Hello", name)

# Converting user input string to int
numberInput = int(input("Enter a number: "))
print(numberInput)
print(type(numberInput))

# Converting user input string to float
numberInput2 = float(input("Enter a float value: "))
print(numberInput2)
print(type(numberInput2))

isValid = bool(input("Enter a boolean: "))
print(isValid)
print(type(isValid))
