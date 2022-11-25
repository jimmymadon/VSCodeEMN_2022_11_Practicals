balance = float(input("Please deposit your starting balance:\n"))

withdrawAmount = float(input("Please enter the amount you want to withdraw:\n"))
if balance >= withdrawAmount:
    balance = balance - withdrawAmount
    print("New balance = ", balance)
else:
    print("Insufficient balance! Your balance is", balance)

depositAmount = float(input("Please enter the amount you want to deposit:\n"))
balance = balance + depositAmount
print("New balance = ", balance)

withdrawAmount = float(input("Please enter the amount you want to withdraw:\n"))
if balance >= withdrawAmount:
    balance = balance - withdrawAmount
    print("New balance = ", balance)
else:
    print("Insufficient balance! Your balance is", balance)

depositAmount = float(input("Please enter the amount you want to deposit:\n"))
balance = balance + depositAmount
print("New balance = ", balance)
