from os import read
import pandas as pd
# Folder relative refrence not work here . so you need to type full refrence
# index_col=0 set first row as header
CSV_PATH = r"C:\Users\rajaa\Desktop\Github Repo\Python-Examples\Python\Pandas\data.csv"
databric = pd.read_csv(CSV_PATH,index_col=0)

# To Display only first 20 rows of csv
print(pd.read_csv(CSV_PATH,nrows=20,index_col=0))
# Get Number of rows and Column in a File
print(databric.shape)
# Print Complete data of  csv
print(databric)
# To Select fews column inside csv
COLTODISPLAY =['id','name','gender','dates','yearOfBirth']
print(pd.read_csv(CSV_PATH,nrows=20,index_col=0,usecols=COLTODISPLAY))
# To Select row by using slices
# print(databric[1:5])
# To Select row and column based on loc
# print(databric.loc[:, ['company', 'length', 'price']])
