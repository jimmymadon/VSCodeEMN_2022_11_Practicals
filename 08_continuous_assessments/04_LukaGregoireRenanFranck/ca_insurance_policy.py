username = input("Welcome on our app. What is your name ?\n")
print("Hello ", username, " ! It's a pleasure to see that you're interested in our services. How can we help you ?")

#We create a loop in order to make sure that the user can re-enter his choice in case of a typing error
while True:
    
    #Ask the user which type of insurance does he want
    print("""
    In order to meet your needs as best as possible, we propose 3 types of insurance :
    1. Car insurance
    2. Home insurance
    3. Mobile phone insurance
    """)
    
    #The user choice is stored into the variable "policychoice"
    policychoice = input("To choose an insurance, please type 1, 2 or 3: \n")
    
    #If the user input anything else than 1, 2 or 3, the loop display the menu to the user one more time
    if not policychoice.isnumeric():
        print("Looks like something went wrong. Please choose an option from the list. And only type the corresponding number.")
        continue
    
    #The policychoice is caracterized as an interger in order to be used in the conditions of the loop
    policychoice = int(policychoice)

    if policychoice > 3 or policychoice < 1:
        print("Looks like something went wrong. Please choose an option from the list. And only type the corresponding number.")
        continue
    
    #The choice is assign to the insurance name in order to be able to be displayed later and to an annual cost to calculate the total cost later
    if policychoice == 1:
        policyname = "Car insurance"
        policycost = int(500)
        policydetails = "500£ per year"
    elif policychoice == 2:
        policyname ="Home insurance"
        policycost = int(1000)
        policydetails = "1000£ per year"
    else:
        policyname = "Mobile phone insurance"
        policycost = int(120)
        policydetails = "10£ per month"
    
    #We create another loop in order to make sure that the user can re-enter his choice in case of a typing error
    while True:
        
        print("Thank you for choosing our services for your", policyname,". How long do you need this services ?")
        
        #Ask the user how long he needs his insurance for
        policyduration = input("Years: \n")
        
        #If the user inputs text, the loop display the menu to the user one more time
        if not policyduration.isnumeric():
            print("Looks like something went wrong. Please the number of years you need your insurance for")
            continue
        
        #The policyduration is caracterized as an interger in order to be used in the conditions of the loop
        policyduration = int(policyduration)

        #If the user inputs a number under 1, the loop display the menu to the user one more time
        if policyduration < 1:
            print("Our services are only available for at least 1 year. Please enter a number of years")
            continue
        
        while True:
            
            #Ask the user which type of payment method he wants to use
            print("Your insurance policy details:",
                "Type:",policyname,
                "Duration:",policyduration,"years."
                """Which payment method would you like to use ? Please see the different options just below :"
                    1. Bank transfer
                    2. Paypal
                    3. Credit Card
                    """)
            
            #The user choice is stored into the variable "paymentchoice"
            paymentchoice = input("To choose a payment method, please type 1, 2 or 3: \n")
            
             #If the user input anything else than 1, 2 or 3, the loop display the menu to the user one more time
            if not paymentchoice.isnumeric():
                print("Looks like something went wrong. Please choose an option from the list. And only type the corresponding number.")
                continue
    
            #The paymentmethod is caracterized as an interger in order to be used in the conditions of the loop
            paymentchoice = int(paymentchoice)

            if paymentchoice > 3 or paymentchoice < 1:
                print("Looks like something went wrong. Please choose an option from the list. And only type the corresponding number.")
                continue
            
            #The choice is assigned to the payment method name in order to be able to be displayed later 
            #and to the transaction fee pourcentage to calculate the total cost later
            #and to the transaction fee details to give a recap to user at the end
            if paymentchoice == 1:
                paymentname = "Bank transfer"
                paymentfee = int(1)
                paymentdetails = "0% fees"
            elif paymentchoice == 2:
                paymentname ="Paypal"
                paymentfee = int(1.1)
                paymentdetails = "10% fees"
            else:
                paymentname = "Credit Card"
                paymentfee = int(1.2)
                paymentdetails = "20% fees"
                
            totalcost = policycost*policyduration*paymentfee
            
            #We use the f-string into "print" in order to make have a better organisation of the variables
            print(f"""
                  Thank you {username} for choosing our services.
                  The total cost of your new {policyname}, is: {totalcost}£
                  Please see below all the details of the insurance policy:
                  Your insurance type : {policyname}
                  Your insurance base premium: {policydetails}
                  The duration of your insurance (in years): {policyduration}
                  Your payment method: {paymentname}
                  Your payment transaction fees: {paymentdetails}
                  The total cost of your insurance: {totalcost}£
                  """)
            
            break
        break
    break