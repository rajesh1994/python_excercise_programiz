"""
Problem Statement : 40. How to check if a dataframe has any missing values?
"""

# Import pandas as pd
import pandas as pd

# Reading data from the CSV file
df1 = pd.read_csv('cars93.csv')
#print(df1)
# Check if df has any missing values
print("Check if df has any missing values:")
print(df1.isnull())
