"""
Problem Statement : 46. How to set the number of rows and columns displayed in the output?
"""
# Import pandas as pd
import pandas as pd

# Reading the CSV file
df1 = pd.read_csv('cars93.csv')

# Change the pandas display settings on printing the dataframe df it shows a maximum of 2 rows and 2 columns.
print("setting the 2 rows & 2 columns to be displayed in the output:")
pd.set_option("display.max_columns", 2)
pd.set_option("display.max_rows", 2)
print(df1)

# Show all available options
# pd.describe_option()
