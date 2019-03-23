"""
Problem Statement : 41. How to count the number of missing values in each column?
"""

# Import pandas as pd
import pandas as pd

# Read data from the CSV file
df1 = pd.read_csv('cars93.csv')

# Number of missing values in each column
num_missing_values_each_cols = df1.apply(lambda x : x .isnull().sum())
print("Number of missing values in each column:")
print(num_missing_values_each_cols.argmax())
