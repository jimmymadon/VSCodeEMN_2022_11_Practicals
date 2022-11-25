# Example of copy-pasting a chunk of lines 3 times
print("Hello, the class of M2 students!")
print("Hope you are enjoying learning Python!")
print()

print("Hello, the class of M2 students!")
print("Hope you are enjoying learning Python!")
print()

print("Hello, the class of M2 students!")
print("Hope you are enjoying learning Python!")
print()

# Instead, we can DEFINE (= create) a function
# This function has no PARAMETERS (= inputs)
def greeting():
    print("Hello, the class of M2 students!")
    print("Hope you are enjoying learning Java!")
    print()

# and then CALL (= running) a function
greeting()
greeting()
greeting()

# This function has two PARAMETERS (= inputs)
def greeting2(className = "M2", programmingLanguage = "Python"):
    print("Hello, the class of", className, "students!")
    print("Hope you are enjoying learning", programmingLanguage, "!")
    print()

# When we call a function, the VALUES we pass to the function are
# called ARGUMENTS
greeting2()
greeting2("U2")
greeting2("M1", "Java")

