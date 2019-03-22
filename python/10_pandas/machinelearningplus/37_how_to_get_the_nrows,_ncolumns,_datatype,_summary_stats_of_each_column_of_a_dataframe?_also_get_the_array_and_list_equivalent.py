"""
Problem Statement : 37. How to get the nrows, ncolumns, datatype, summary stats of each column of a dataframe? Also get the array and list equivalent.
"""

# Import pandas as pd
# Import numpy as np
import pandas as pd
import numpy as np

# Reading the csv file
df = pd.read_csv('cars93.csv')

# Number of rows & columns
print("Number of rows & columns:")
print(df.shape)

# Data-type
print("\nData-type:")
print(df.dtypes)

# How many columns under each datatype
print("\nHow many columns under each datatype:")
print(df.get_dtype_counts())
print(df.dtypes.value_counts())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Numpy array
print("\nNumpy array:")
print(df.values)
"""
# List
print("\nList:")
print(df.values.tolist())
"""
