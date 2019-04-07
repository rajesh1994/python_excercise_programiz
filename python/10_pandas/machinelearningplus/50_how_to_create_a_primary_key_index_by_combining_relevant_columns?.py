"""
Problem Statement : 50. How to create a primary key index by combining relevant columns?
"""

# Import pandas as pd
import pandas as pd

# Reading the CSV file
df = pd.read_csv('cars93.csv', usecols = [0, 1, 2, 3, 4, 5])
print("The df is:")
print(df.head(10))

# In df, Replace NaNs with ‘missing’ in columns 'Manufacturer', 'Model' and 'Type' and create a index as a combination of these three columns and check if the index is a primary key.

df[['Manufacturer', 'Model', 'Type']] = df[['Manufacturer', 'Model', 'Type']].fillna('Missing')
df.index = df.Manufacturer + '_' + df.Model + '_' + 'Type'
print("\nThe Expected Output:")
print(df.head(10))
print("\nThe index primary key status:", df.index.is_unique)
