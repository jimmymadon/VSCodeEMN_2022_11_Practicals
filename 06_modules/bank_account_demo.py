import bank_account

balance = float(input("Please deposit your starting balance:\n"))

balance = bank_account.withdraw(balance)
balance = bank_account.deposit(balance)

balance = bank_account.withdraw(balance)
balance = bank_account.deposit(balance)
