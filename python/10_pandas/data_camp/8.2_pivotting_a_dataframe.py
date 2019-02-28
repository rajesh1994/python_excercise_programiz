"""
Problem Statement : 8.2 Pivotting a DataFrame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame({'category' : ['Cleaning', 'Cleaning', 'Entertainment', 'Entertainment', 'Tech', 'Tech'], 'store' : ['Walmart', 'Dia', 'Walmart', 'Fnac', 'Dia', 'Walmart'], 'price' : [11.42, 23.50, 19.99, 15.95, 55.75, 111.55], 'testscore' : [4, 3, 5, 7, 5, 8]})
print("DataFrame 'df' is:")
print(df)

pivot_df = df.pivot_table(index = 'category', columns = 'store', values = 'price', aggfunc = 'mean')
print("Pivotting a DataFrame:")
print(pivot_df)
