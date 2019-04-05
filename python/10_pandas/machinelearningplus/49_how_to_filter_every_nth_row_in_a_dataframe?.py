"""
Problem Statement : 49. How to filter every nth row in a dataframe?
"""

# Import pandas as pd
import pandas as pd

# Initialize DataFrame df
df = pd.read_csv("cars93.csv")

# From df, filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
print("Filter every 20th row in a dataframe:")
print(df.iloc[::20 , :][['Manufacturer', 'Model', 'Type']])
