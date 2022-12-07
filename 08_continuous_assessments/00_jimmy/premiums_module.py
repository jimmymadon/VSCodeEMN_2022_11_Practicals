from helper_functions import get_valid_int_input, get_valid_float_input


def calculate_premiums():
    print()
    number_of_policies = get_valid_int_input(
        "How many Insurance Premiums do you want to calculate? Enter a number: ")

    premiums_sum = 0
    largest_premium = 0
    for index in range(number_of_policies):
        premium = get_valid_float_input(
            "Please insert your Insurance Premium: ")
        premiums_sum += premium
        if largest_premium < premium:
            largest_premium = premium

    average_premium = premiums_sum/number_of_policies

    print()
    print("The sum of all your premiums is: £", premiums_sum)
    print("The average of all your premiums is: £", average_premium)
    print("Your largest premium is: £", largest_premium)
    print()
