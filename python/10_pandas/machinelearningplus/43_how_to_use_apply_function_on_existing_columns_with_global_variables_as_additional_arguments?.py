"""
Problem Statement : 43. How to use apply function on existing columns with global variables as additional arguments?
"""

# Import pandas as pd
# import numpy as np
import pandas as pd
import numpy as np

# Read data from CSV file
df1 = pd.read_csv('cars93.csv', usecols = ['Min.Price', 'Max.Price'])
print("Data from the CSV file:")
print(df1.head())

d = {'Min.Price' : np.nanmean, 'Max.Price' : np.nanmedian}
df1[['Min.Price', 'Max.Price']] = df1[['Min.Price', 'Max.Price']].apply(lambda x, d : x.fillna(d[x.name](x)), args = (d, ))
print(df1[['Min.Price', 'Max.Price']].head())
