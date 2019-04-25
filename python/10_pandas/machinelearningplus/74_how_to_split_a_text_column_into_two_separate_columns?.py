"""
Problem Statement : 74. How to split a text column into two separate columns?
"""

# Import pandas as pd
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(["STD, City	State", "33, Kolkata	West Bengal", "44, Chennai	Tamil Nadu", "40, Hydrabad	Telangana", "80, Bangalore	Karnataka"], columns = ['row'])
print("DataFrame 'df':")
print(df)
# Split a text column into two separate columns
df_out = df.row.str.split(',|\t', expand = True)

# Make first as header
new_header = df_out.iloc[0]
df_out = df_out[1 :]
df_out.columns = new_header
print("\nSplit a text column into two separate columns:")
print(df_out)
