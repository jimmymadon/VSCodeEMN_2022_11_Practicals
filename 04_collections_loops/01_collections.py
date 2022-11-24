# Below four lines show 4 disconnected individual variables.
# Hence, for related data, we use Collections (Lists, Tuples, Sets, Dictionaries)
marks1 = 100
marks2 = 67
marks3 = 79
marks10 = 67
print("Variable marks3: ", marks3)
print("Variable marks10:", marks10)
print()

## Lists

# Below we create a list
print("*** Creating a list with 5 elements ***")
marks = [100, 67, 79, 67]
print("Type of collection marks is: ", type(marks))
print()

print("Printing the whole list")
print(marks)
print()

print("Accessing individual items of marks")
print("Third element in marks is marks[2]: ", marks[2])
print("Fourth element in marks is marks[3]: ", marks[3])
print()

print("Modifying the fourth element")
marks[3] = 89
print("Printing the updated list...")
print(marks)
print()

print("Type of marks[3]:", type(marks[3]))
print()

print("Length of the marks list is:", len(marks))
print()

print("*** Appending items to the END of marks using append() function ***")
marks.append(50)
print("List after appending...", marks)
print("Length of marks is now", len(marks))
print()

print("Lists can contain multiple types of data")
marks.append("Jimmy") # Appending a string
print(marks)
print()

print("Inserting items in between a list using insert() function")
marks.insert(2, 35)
print("Updated marks:", marks)
print()

print("*** Fun with lists ***")
print("Check if Jimmy exists in list:", marks.count("Jimmy"))
print("Check if Gregoire exists in list:", marks.count("Gregoire"))
print()

if marks.count(100) > 0:
    print("Hurray!")
print()

print("Removing element 3 in marks using pop() function:", marks.pop(2))
print("Updated list:", marks)
print()

# Using negative indexes to iterate lists from their END
print("Second last item in the list:", marks[-2])
marksLength = len(marks)
print("Second last item in the list:", marks[marksLength - 2])
