#We create the list
list_premium=[]

#We ask the user to input his premiums, separated by spaces
premiums=input("Hello, please enter a list of insurance premiums. The number sequence must be separated by spaces: ")

#All the premiums are integrated into the list. The split allow the user to put all the premiums but the program still serperate the numbers
list_premium = [int(i) for i in premiums.split()]

#We create 3 variables in order to create the formulas and to make it easier to display in the "print" at the end
sum_premiums = sum(list_premium)
mean_premiums = sum_premiums / len(list_premium)
max_premiums = max(list_premium)

print ("You entered the following list of premiums:",list_premium)
print ("The sum of all the premiums you entered is:",sum_premiums)
print ("The mean of all the premiums you entered is:",mean_premiums)
print ("The max of all the premiums you entered is:",max_premiums)
