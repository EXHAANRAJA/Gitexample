from os import read
import pandas as pd
# Folder relative refrence not work here . so you need to type full refrence
# index_col=0 set first row as header
databric = pd.read_csv(r"D:\GIT Work\Python\Pandas\data.csv", index_col=0)

# Get Number of rows and Column in a File
print(databric.shape)

# Print data inside csv
print(databric)

# To Select any single column inside csv
print(databric[["wheel-base"]])

# To Select row by using slices
print(databric[1:5])

# To Select row and column based on loc

print(databric.loc[:, ['company', 'length', 'price']])
