accountBalance = 10   # Variable of the type integer
print("Account Balance is:", accountBalance)
print("Type of accountBalance is", type(accountBalance))
print() # Empty print function returns a new line

accountBalance = accountBalance + 10 # Example of variable changing value
print("New account balance is:", accountBalance)
print()

distance = 10.9 # Variable of type float
print("Distance is", distance, "kilometres.")
print("Type of:", type(distance))
print()

divisionResult = 3/2
print("3/2 is:", divisionResult)
print("Type of divisionResult is:", type(divisionResult))

message = "Hello"     # Variable of the type string (str)
message = 'Hello'     # Using single or double quotes is the same for strings
print("Message is", message)
print('Type of:', type(message))
print()

isValid = True # Variable of the type boolean (bool)
print("isValid is:", isValid)
print("Type of isValid:", type(isValid))
isValid = False
print("isValid is:", isValid)

# Be careful of type changes
startingBalance = 100
startingBalance = "Error! No starting balance found"
finalBalance = startingBalance + 50 # TypeError - cannot concatenate str with int
print("Final Balance is", finalBalance)
