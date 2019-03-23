"""
Problem Statement : 38. How to extract the row and column number of a particular cell with given criterion?
"""

# Import pandas as pd
# Import numpy as np
import pandas as pd
import numpy as np

# Reading the csv file
df1 = pd.read_csv('cars93.csv')

# Get manufacturer with highest price
print("\nManufacturer with highest price:")
print(df1.loc[df1.Price == np.max(df1.Price), ['Manufacturer', 'Model', 'Type']])

# Get row & column number
print("\nRow & column number of highest price:")
row, col = np.where(df1.values == np.max(df1.Price))
print(row, col)

# Get the values of highest price
print("\nValues of highest price:")
print(df1.iat[row[0], col[0]])
print(df1.iloc[row[0], col[0]])

# Alternates
#print(df1.at[row[0], 'Price'])
#print(df1.get_value(row[0], 'Price'))
