"""
Problem Statement : 34. How to change column values when importing csv to a dataframe?
"""

# Import pandas as pd
import pandas as pd

# Method 1 : Using converter parameter
# Initialize DataFrame 'df1'
df1 = pd.read_csv('boston_housing.csv', converters = {'medv' : lambda x : 'High' if float(x) > 25 else 'Low'})
print('Method 1 : Using converter parameter:\nchange column values when importing csv to a dataframe:')
print(df1.head())

# Method 2 : Using CSV reader
import csv
with open('boston_housing.csv', 'r') as f:
	reader = csv.reader(f)
	out = []
	for i, row in enumerate(reader):
		if i > 0:
			row[13] = 'High' if float(row[13]) > 25 else 'Low'
		out.append(row)
df1 = pd.DataFrame(out[1:], columns = out[0])
print('\nMethod 2 : Using CSV reader:\nchange column values when importing csv to a dataframe:')
print(df1.head())
