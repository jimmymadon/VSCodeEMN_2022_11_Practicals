#Simple list
car_models_list = ['C Class', '3 Series', 'Q7', 'Aventador']
print(car_models_list[1]) # key is 1 (in a list, keys are added by python automatically)
print(car_models_list)

# Simple dictionary
cars_dictionary = {
    'Mercedes Benz': 'C Class', # key = 'Mercedes Benz', value = 'C Class'
    'BMW': '3 Series',
    'Audi': 'Q7',
    'Lamborghini': 'Aventador'
}
print(cars_dictionary)
print(cars_dictionary['Lamborghini']) # Print value using the key

for value in car_models_list:
    print(value)

for key in cars_dictionary:
    print(key)
    print(cars_dictionary[key])

