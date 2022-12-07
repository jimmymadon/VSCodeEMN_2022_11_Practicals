def get_valid_int_input(message):
    while True:
        try:
            input_integer = int(input(message))
            return input_integer
        except ValueError:
            print("Invalid option, please enter an integer value.")
            continue


def get_valid_float_input(message):
    while True:
        try:
            input_float = float(input(message))
            return input_float
        except ValueError:
            print("Invalid option, please enter a float value.")
            continue
