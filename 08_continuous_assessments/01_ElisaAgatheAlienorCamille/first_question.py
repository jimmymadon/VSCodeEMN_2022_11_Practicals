from function1 import user_input # In order to use the functions defined in the file 'function1', we import it in this file
                                                                                                     
# First step : Ask the user's policy personal details :
Name = input("Please enter your name:\n") # The user can enter his name thanks to the input function
Duration = float(input("Please enter the duration of your insurance policy in number of years:\n")) # Float function converts the specified value into a floating point number


# Ask the user's policy type,  we use a menu to let the user chose his policy type
print("""
Policy types' menu:
1. Car Insurance
2. Home Insurance
3. Mobile Phone Insurance
4. Quit
""")
 
policyType = user_input() # We use the function 'user_input' as seen in the file 'function1' to run the program
print()                               # It will allow the user to choose between the 4 options offered in the menu

 
# Ask the user's payment type, we use a menu to let the user chose his payment type
print("""
Payment types' menu:
1. Bank Transfer
2. PayPal
3. Credit Card
4. Quit
""")

paymentType = user_input() # We use the function 'user_input' as seen in the file 'function1' to run the program
print()                                 # It will allow the user to choose between the 4 options offered in the menu


# Calculation of the total cost of the insurance policy for the entire duration of the policy
# We use a if condition to associate the base premium according to the user's choice of policy type
if policyType == 1:              # 1 means "Car Insurance", so the premium associated is 500 £ per year
    BasePremium = 500
elif policyType == 2:            # 2 means "Home Insurance", so the premium associated is 1000 £ per year
    BasePremium = 1000  
else:                            # 3 means "Mobile Phone Insurance", so the premium associated is 10 £ per month 
    BasePremium = 10*12          # Then, we multiply by 12 to express the amount per year
 
                                 
# We use a if condition to associate the transaction fees according to the user's choice of payment type
if paymentType == 1:
    TransactionFee = 0           # no fee
elif paymentType == 2:
    TransactionFee = 0.1         # 0.1 means 10%
else:
    TransactionFee = 0.2         # 0.2 means 20%
   

# Print of all the information chosen precedently
# We use a if conditions to fill in the details' sentence with the right policy type
if policyType == 1:
    policyType = 'Car insurance'
elif policyType == 2:
    policyType = 'Home insurance'
else:    
    policyType = 'Mobile Phone insurance'
 
# We use a if conditions to fill in the details' sentence with the right payment type
if paymentType == 1:
    paymentType = 'Bank Transfer'
elif paymentType == 2:
    paymentType = 'PayPal'
else:
    paymentType = 'Credit Card'
 
# We wrap up all the user's selected options in a sentence 
print("Dear", Name,"you have chosen:", policyType, "&", paymentType, "for a duration of", Duration, "years.")
print()
 
# We calculate the total cost with the base premium associated to the policy type chosen, the transaction fee associated
# to the payment type chosen and the duration manually entered by the user
print("The total cost is:", (BasePremium*(1+ TransactionFee))*Duration, "£.")
print()