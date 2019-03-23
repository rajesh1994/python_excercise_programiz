"""
Problem Statement : 39. How to rename a specific columns in a dataframe?
"""

# Import pandas as pd
import pandas as pd

# Read data from the CSV file
df1 = pd.read_csv('cars93.csv')
#print(df1)

# Method 1 : Rename a coulumn type as Car_Type
print("Method 1 : Rename a coulumn type as Car_Type:")
df1=df1.rename(columns = {'Type':'CarType'})
print(df1.head())
"""
# Method 2 : Rename a coulumn type as Car_Type
print("Method 2 : Rename a coulumn type as Car_Type")
df1.columns.values[2] = 'Car_Type1'
print(df1.coulumns.valus[2])
"""
# Replace the ‘.’ in column names with ‘_’
df1.columns = df1.columns.map(lambda x : x.replace('.', '_'))
print("\nReplace the ‘.’ in column names with ‘_’:")
print(df1.columns)
