import pandas as pd

car_manufacturers = ['Mercedes', 'BMW', 'Audi', 'Citroen', 'Renault']
print('Printing car_manufacturers')
print(car_manufacturers)
print('Type of car_manufacturers:', type(car_manufacturers))
print()

print('Create and print a Pandas Series using a list')
car_manufacturers_series = pd.Series(car_manufacturers)
print(car_manufacturers_series)
print('Type of car_manufacturers_series:', type(car_manufacturers_series))
print('Fourth car in the series:', car_manufacturers_series[3])
print()

car_models = ['C Class', '3 Series', 'Q7', 'C3', 'Megane']

cars_series = pd.Series(car_models, car_manufacturers)
print('Printing cars_series')
print(cars_series)
print(cars_series['Renault'])
print()

cars_dictionary = {
    'Mercedes': 'C Class',
    'BMW': '3 Series',
    'Audi': 'Q7'
}
cars_series_2 = pd.Series(cars_dictionary)
print(cars_series_2)
