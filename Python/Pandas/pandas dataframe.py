import pandas as pd
names = ['United States', 'Australia', 'Japan',
         'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
cars = pd.DataFrame(my_dict)

# Set the row label ,Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels

print(cars)

# We can used number of scalar function inside pandas dataframe

cars['cars_per_cap'].max  # Display max number inside list
cars['cars_per_cap'].min  # Display min number inside list

# or by using series
print(cars.max())
print(cars.min())

# to display statistical component
print(cars.describe())

# During Pandas Dataframe first 5 and last 5 rows display by default
cars.head(8)  # Display first 8 rows
print(cars.dtypes) # Display column datatype
print(cars.info())  # Print Column name,Not Null Statistics and Datatype
print(type(cars))  # Display dataframe
print(cars['country']) # each individual column display a series

print(cars['cars_per_cap'] < 500)
