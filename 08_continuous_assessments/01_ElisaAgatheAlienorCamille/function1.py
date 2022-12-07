def user_input(): # define the function used in the main file "first question"
    while True: # define the loop 
        Type = input("Please enter an option between 1 and 4:\n") # Ask the number of the menu
        if not Type.isnumeric(): # check if the input is numeric, otherwise ask again 
            print("Please enter a valid digit!")
            continue

        Type = int(Type) # define the type integer to the input menu's number 

        if Type > 4 or Type < 1: # verify that the number is between 1 and 4, otherwise ask again
            print("Please enter a valid option!")
            continue

        if Type == 4: # we add an option to exit the program with the number 4
            print("Exit of the program")
            exit()
        
        break # stop the loop
    return Type # make the function send Python object back to the caller code ("first question")