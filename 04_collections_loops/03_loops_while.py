print("for loop to print 0 - 9")
for number in range(10):
    print(number)

print("while loop to print 0 - 9")
counter = 0
while counter < 10:
    print(counter)
    counter = counter + 1

print("Using the break statement at the start of an infinite loop")
counter = 0
while True:
    if counter == 10:
        break
    print(counter)
    counter = counter + 1
