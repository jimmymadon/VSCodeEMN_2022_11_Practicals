from policy_module import get_users_policy_type, get_users_payment_type, calculate_fee, calculate_policy_base_cost
from helper_functions import get_valid_int_input
from premiums_module import calculate_premiums

print("** Welcome to our Insurance App **")
user_name = str(input("Please enter your name: "))
print("Hello " + user_name + "!")

policy_type = get_users_policy_type()

policy_duration = get_valid_int_input(
    "Please insert the duration of your insurance policy (in years): ")

base_cost = calculate_policy_base_cost(policy_type, policy_duration)

payment_type = get_users_payment_type()

calculate_fee(base_cost, payment_type)

calculate_premiums()
