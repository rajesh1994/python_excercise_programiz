"""
Problem Statement : 33. How to import only every nth row from a csv file to create a dataframe?
"""

# Import pandas as pd
import pandas as pd

# Method 1 : Using chunks and for-loop
# Initialize DataFrame 'df'
df1 = pd.read_csv('boston_housing.csv', chunksize= 50)
df2 = pd.DataFrame()
for chunk in df1:
	df2 = df2.append(chunk.iloc[0, :])
# Import only every 50th row from a csv file to create a dataframe
print("Method 1 : Using chunks and for-loop\nImport only every 50th row from a csv file to create a dataframe:")
print(df2)
"""
# Method 2 : Using chunks & list comprehension
df1 = pd.read_csv('boston_housing.csv', chunksize = 50)
df2 = pd.concat([chunk.iloc[0] for chunk in df1], axis = 0)
df2 = df2.transpose()
print("Method 2 : Using chunks & list comprehension\nImport only every 50th row from a csv file to create a dataframe:")
print(df2)
"""
# Method 3 : Using CSV reader
import csv
with open('boston_housing.csv', 'r') as f:
	reader = csv.reader(f)
	out = []
	for i, row in enumerate(reader):
		if i % 50 == 0:
			out.append(row)
df1 = pd.DataFrame(out[1:], columns = out[0])
print("\nMethod 3 : Using CSV reader\nImport only every 50th row from a csv file to create a dataframe:")
print(df1)
