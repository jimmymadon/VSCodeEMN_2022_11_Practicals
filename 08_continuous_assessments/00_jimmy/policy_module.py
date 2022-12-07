from helper_functions import get_valid_int_input


def get_users_policy_type():
    valid_policy_types = [1, 2, 3]
    while True:
        print("""
        Policy types:
        1: Car Insurance
        2: Home insurance
        3: Mobile phone Insurance
        """)

        policy_type = get_valid_int_input("Please choose a Policy Type: ")

        if policy_type in valid_policy_types:
            # the return statement automatically exits the whole function, and hence the loop as well!
            return policy_type

        # if we reach this line, then policy_type is NOT in valid_policy_types
        print("Invalid Policy Type, please try again!")


def get_users_payment_type():
    valid_payment_types = [1, 2, 3]
    while True:
        print("""
        Payment types:
        1: Bank Transfer
        2: Paypal
        3: Credit Card
        """)

        payment_type = get_valid_int_input("Please choose a payment type: ")

        if payment_type in valid_payment_types:
            # the return statement automatically exits the whole function, and hence the loop as well!
            return payment_type

        # if we reach this line, then payment_type is NOT in valid_payment_types
        print("Invalid Payment Type, please try again!")


def calculate_policy_base_cost(policy_type, policy_duration):
    policy_type_costs = {
        1: (500, "The yearly premium before payment fee for your car insurance will be: £"),
        2: (1000, "The yearly premium before payment fee for your home insurance will be: £"),
        3: (120, "The yearly premium before payment fee for your mobile insurance will be: £"),
    }
    base_cost = policy_duration * policy_type_costs[policy_type][0]
    print(policy_type_costs[policy_type][1], base_cost)
    return base_cost


def calculate_fee(base_cost, payment_type):
    payment_type_fees = {
        1: (1, "There is no additional fee, the total yearly fee for your insurance will be: £"),
        2: (1.1, "There is an additional fee with this payment type of 10%, the total yearly fee for your insurance will be: £"),
        3: (1.2, "There is an additional fee with this payment type of 20%, the total yearly fee for your insurance will be: £"),
    }

    new_cost = base_cost * payment_type_fees[payment_type][0]
    print(payment_type_fees[payment_type][1], new_cost)
