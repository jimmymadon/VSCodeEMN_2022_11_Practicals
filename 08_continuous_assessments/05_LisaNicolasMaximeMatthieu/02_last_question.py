# creating an empty list
insurancePremiums = []
  
# number of elements as input
list_numbers = int(input("How many insurance premiums do you want to enter in the list ?\n "))
print()
print("______________________________________________")
print()

print("Please enter your", list_numbers, "insurance premiums:\n")

# iterating till the range
for i in range(0,list_numbers):
    premium = int(input())

    insurancePremiums.append(premium) # adding the element

print()
print("______________________________________________")
print()

print("You have chosen the following insurance premiums",insurancePremiums);
print()

print("The sum of the insurance premiums of the list are: ")
print(sum(insurancePremiums))
print()

print("The highest insurance premium of the list is: ")
print(max(insurancePremiums))
print()

print("The lowest insurance premium of the list is: ")
print(min(insurancePremiums))
print()


print("The average insurance premium of the list is: ")
print(sum(insurancePremiums)/len(insurancePremiums))
print()