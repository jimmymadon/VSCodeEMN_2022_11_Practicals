# Function definitions
def withdraw(pBalance = 0):
    withdrawAmount = float(input("Please enter the amount you want to withdraw:\n"))
    if pBalance >= withdrawAmount:
        pBalance = pBalance - withdrawAmount
        print("New balance = ", pBalance)
    else:
        print("Insufficient balance! Your balance is", pBalance)

    return pBalance

def deposit(pBalance = 0):
    depositAmount = float(input("Please enter the amount you want to deposit:\n"))
    pBalance = pBalance + depositAmount
    print("New balance = ", pBalance)
    return pBalance

# Program begins here
balance = float(input("Please deposit your starting balance:\n"))

balance = withdraw(balance)
balance = deposit(balance)

balance = withdraw(balance)
balance = deposit(balance)
