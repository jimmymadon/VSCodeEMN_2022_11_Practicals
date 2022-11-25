def withdraw(pBalance):
    withdrawAmount = float(input("Please enter the amount you want to withdraw:\n"))
    if pBalance >= withdrawAmount:
        pBalance = pBalance - withdrawAmount
        print("New balance = ", pBalance)
    else:
        print("Insufficient balance! Your balance is", pBalance)

    return pBalance

def deposit(pBalance):
    depositAmount = float(input("Please enter the amount you want to deposit:\n"))
    pBalance = pBalance + depositAmount
    print("New balance = ", pBalance)
    return pBalance
