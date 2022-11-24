studentsMarks = [95, 89, 78, 57, 90]

print("***Printing items of studentsMarks individually***")
print(studentsMarks[0])
print(studentsMarks[1])
print(studentsMarks[2])
print(studentsMarks[3])
print(studentsMarks[4])
print() # Prints an empty line

print("***Printing all items in studentsMarks using for loop***")
for studentMarks in studentsMarks:
    print(studentMarks)

print()

print("***Sum of all the marks***")
totalMarks = 0
for studentMarks in studentsMarks:
    totalMarks = totalMarks + studentMarks

print("Total marks:", totalMarks)
print("Average of all studentsMarks:", totalMarks/len(studentsMarks))
print()

print("***Highest marks***")
highestMarks = studentsMarks[0]
for studentMarks in studentsMarks:
    if studentMarks > highestMarks:
        highestMarks = studentMarks
print("Highest Marks is:", highestMarks)
print()

print("***Lowest marks***")
lowestMarks = studentsMarks[0]
for studentMarks in studentsMarks:
    if studentMarks < lowestMarks:
        lowestMarks = studentMarks

print("Lowest Marks is:", lowestMarks)
print()

# Printing Hello World five times using your own random list of 5 numbers
list5 = [1, 2, 3, 4, 5]
for listItem in list5:
    print("Hello World")

print()

# Instead, range() allows us to create a list of numbers easily
for rangeItem in range(5):
    print("Hello World")
    if rangeItem == 3:
        break # break exits the current iteration and all further iterations
    print(rangeItem)

print()

# continue exits the current iteration BUT continues further iterations
for rangeItem in range(5):
    print("Hello World")
    if rangeItem == 3:
        continue
    print(rangeItem)
    print("Something Else")

print()

# Printing individual letters of a string
# "for" loops works with ANY collection: lists, tuples, sets, dictionaries
# and strings.
for char in "Jimmy":
    print(char)

print()

students = ["Jimmy", "Gregoire", "Agathe", "Riccardo", "Luka"]

# Example of manually using index to print elements
# Prints only the first two names of a list
index = 0
for student in students:
    if index == 2:
        break
    print(students[index]) # print(student)
    index += 1 # index = index + 1

# Print only names of students with an even index
index = 0
for student in students:
    if index % 2 == 0:
        print(students[index]) # print(student)
    index += 1 # index = index + 1

# Example of nested loops.
for student in students:
    for letter in student:
        if letter == 'i':
            break # The break statement exits the nearest loop
        print(letter)
