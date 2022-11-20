marks = input("Please enter your marks: ")

if not marks.isnumeric():
    print("Please enter a valid number.")
    exit()

marks = float(marks)

# Method 2: Similar to above but remove elif - else and use exit() instead.
# This method will not execute further if it reaches any exit() function.
if marks > 100 or marks < 0:
    print("Incorrect marks.")
    exit()

if marks >= 70:
    print("Distinction")
    exit()

if marks >= 40:
    print("Pass")
    exit()

print("Fail")

