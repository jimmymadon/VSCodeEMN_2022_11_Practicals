accountBalance = 500
withdrawAmount = float(input("How much money do you want to withdraw?"))

# Method 1 - Using if and else
# if accountBalance >= withdrawAmount:
#     accountBalance = accountBalance - withdrawAmount
#     print("Your new balance is:", accountBalance)
# else:
#     print("Sorry! You do not have enough money!")
#     print("You can withdraw a max amount of:", accountBalance)

# Method 2 - Remove else and exit early if accountBalance >= withdrawAmount:
if accountBalance >= withdrawAmount:
    accountBalance = accountBalance - withdrawAmount
    print("Your new balance is:", accountBalance)
    exit()

print("Sorry! You do not have enough money!")
print("You can withdraw a max amount of:", accountBalance)
