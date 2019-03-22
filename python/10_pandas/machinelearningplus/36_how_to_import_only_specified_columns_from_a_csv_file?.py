"""
Problem Statement : 36. How to import only specified columns from a csv file?
"""

# Import pandas as pd
import pandas as pd

# Import 'rm', 'age', 'medv' columns from a csv file
df1 = pd.read_csv('boston_housing.csv', usecols = ['rm', 'age', 'medv'])
print("Import 'rm', 'age', 'medv' columns from a csv file:")
print(df1.head())
