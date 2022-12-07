#Ask the user to enter the insurance premiums separated by a coma
premiums = input("Hello, please enter your list of insurance premiums separated by a coma:\n")
 
#Creation of the list form by the premiums
List_premiums = premiums.split(',')
 
#Show the list of premiums
print("You have chosen these following insurance premiums:",List_premiums)
print()
 
float_List_premiums = [float(n) for n in List_premiums] #for n a premiums in the list, it becomes a number and not a string anymore
 
#Sum of the numbers of the list with the function sum
print("The sum of your list of premiums is:",sum(float_List_premiums))
print()
 
#Mean of the numbers with function sum & function len (it is giving the number of item in the list)
mean = sum(float_List_premiums)/len(float_List_premiums)
print("The average of your list of premiums is:", mean)
print()
 
#Use of the function max to print the maximum value of the list
print("The value of the maximum premium is:", max(float_List_premiums))