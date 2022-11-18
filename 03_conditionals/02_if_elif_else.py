marks = float(input("Please enter your marks: "))

# Example of the "number-line" that I drew in my head for this program
# -infinity, 0, 40, 60, 70, 100, +infinity
# In such cases, always check that the WHOLE number line is taken care by your program.

# Method 1: The below code uses ONE if-elif-else block
if marks > 100 or marks < 0:
    print("Incorrect marks.")
elif marks >= 70:
    print("Distinction")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

