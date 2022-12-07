premium = 0
fee = 0

# Welcome message - Website homepage --------------------------------------------------------------------------------

while True:
    print()
    print("__________________________")
    print()

    print("Welcome to Admiral Insurance")
    print()

    # Creation of an account - beginning of a new loop ----------------------------------------------------------------

    while True:
        newAccount = input("Would you like to create an account? (Yes or No)\n")
        print()
        print("__________________________")
        print()

        if newAccount == "Yes" or newAccount == "yes":

            firstName = input("Great! Please insert your first name:\n")

            while firstName[0] != firstName[0].upper() or firstName.isdigit() :
                print("Error!")
                firstName = input("Please insert your first name: \n")

            lastName = input("... And your last name:\n")
            print()

            while lastName[0] != lastName[0].upper() or lastName.isdigit() :
                print("Error!")
                lastName = input("Please insert your last name.\n")
                print()

            print("Account was succesfully created. Good to see you", firstName,"!")
            print()
            print("__________________________")
            print()
        elif newAccount == "No" or newAccount == "no":
            print("No account has been created.")
            break
        else:
            print("Error. Please make sure to enter a valid option.")
            print()
            continue

        counter = 0

        while True:

            if counter ==0:

                aPolicy = input("Do you wish to create an Insurance Policy : Yes or No\n")
                print()
                print("__________________________")
                print()

                if aPolicy == "Yes" or aPolicy == "yes":
                    print("Good, we will happily guide you through this process!")
                elif aPolicy == "No" or aPolicy == "no":
                    print("Exiting... Thank you for visiting!")
                    print()
                    break
                else:
                    print("Error. Please insert Yes or No.")
                    continue
            elif counter >0:
                aPolicy = input("Would you like to create another insurance policy?\n")
                print()
                if aPolicy == "Yes" or aPolicy == "yes":
                    print("Let's do this!")
                elif aPolicy == "No" or aPolicy == "no":
                    print("Thank you for trusting us. Come back anytime!")
                    print()
                    print("__________________________")
                    print()
                    break
                else:
                    print("Error. Please insert Yes or No.")
                    continue

            print()
            print("__________________________")

            # Policy type -------------------------------------------------------------------------------------------------------

            while True:

                print("""
                1. Car Insurance
                2. Home Insurance
                3. Mobile Phone Insurance
                4. Cancel
                """)

                policyInput = input("Now please select the type of policy you would like to choose (1,2,3 or 4). ")
                print()

                if not policyInput.isnumeric():
                    print("Please enter a valid option.")
                    continue

                policyInput = int(policyInput)

                if policyInput > 4 or policyInput < 1:
                    print("Please enter a valid option.") 
                    continue

                print("__________________________")
                print()

                if policyInput == 1:
                    policy = 'Car Insurance'
                    print("You chose to create a new", policy, "policy")
                    print()
                    break
                elif policyInput == 2:
                    policy = "Home Insurance"
                    print("You chose to create a new", policy, "policy")
                    print()
                    break
                elif policyInput == 3:
                    policy = "Mobile Phone Insurance"
                    print("You chose to create a new", policy, "policy")
                    print()
                    break
                elif policyInput == 4:
                    print("Process has been cancelled and no insurance policy has been created. Thank you for your visit!")
                    print()
                    print("__________________________")
                    print()
                    exit()
                
            # Duration of the policy -------------------------------------------------------------------------------------------------
            print()

            durationInput = input("Please insert the requested duration of your policy (in years):\n")
            print()   

            if durationInput.isdigit() or float(durationInput)>0:
                durationInput = float(durationInput)
                print("The duration of the policy will be of", durationInput,"years.")
                print()
            else:
                print("Please enter a valid digit!")
                exit()

            print()

            if policyInput == 1:
                premium += (500 / 12) * (durationInput * 12)
            elif policyInput == 2:
                premium += (1000 / 12) * (durationInput * 12)
            elif policyInput == 3:
                premium += (120 / 12) * (durationInput * 12)


            print("The cost of such policy will be of", round(premium,2),'£ (fees not included).')
            print()
            print("__________________")

            # Payment method -------------------------------------------------------------------------------------------------------

            print("""
            1. Bank transfer
            2. PayPal
            3. Credit Card
            4. Cancel
            """)

            while True:
                paymentMethod = input("How would like to pay? Be aware that fees may apply.")
                print()
                print("__________________")
                print()

                if paymentMethod == "1":
                    payment = "Bank transfer"
                    print("You chose", payment, "as your payment method.")
                    fee = 1.0 # 0% fee
                    break
                elif paymentMethod == "2":
                    payment =  "PayPal"
                    print("You chose", payment, "as your payment method.")
                    fee = 1.10
                    break
                elif paymentMethod == "3":
                    payment = "Credit Card"
                    print("You chose", payment, "as your payment method.")
                    fee= 1.2
                    break
                elif paymentMethod == "4":
                    print("Process has been cancelled. Thank you for your visit. Try again anytime!")
                    print()
                    print("__________________")
                    print()
                    exit()
                else:
                    print("Error, please insert a valid option.")
                    continue

            totalPrice = premium * fee
            totalPrice = round(totalPrice,2)

            # Summary -------------------------------------------------------------------------------------------------------------------------------

            print("Dear", firstName, ", you asked for a", durationInput,"years",policy,"contract. The total cost using",payment,"is £",totalPrice)
            print()
            print("Thank you for trusting us!")
            print()
            print("__________________")
            print()

            counter += 1
