def addition(pNumber1, pNumber2):
    return pNumber1 + pNumber2

def subtraction(pNumber1, pNumber2):
    return pNumber1 - pNumber2

def multiplication(pNumber1, pNumber2):
    return pNumber1 * pNumber2

def division(pNumber1, pNumber2):
    return round(pNumber1 / pNumber2, 2)

def isOptionValid(pMenuOption):
    if not pMenuOption.isnumeric():
        print("Please enter a valid digit!")
        return False

    pMenuOption = int(pMenuOption)
    if pMenuOption > 5 or pMenuOption < 1:
        print("Please enter a valid option!")
        return False

    return True
