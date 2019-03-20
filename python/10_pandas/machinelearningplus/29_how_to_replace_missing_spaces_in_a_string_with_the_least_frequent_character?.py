"""
Problem Statement : 29. How to replace missing spaces in a string with the least frequent character?
"""
# Import pandas as pd
import pandas as pd

# Initialize series1
series1 =  pd.Series(list('dbc deb abed gade'))
freq = series1.value_counts()
print(freq)
least_freq = freq.dropna().index[-1]
print(least_freq)

print("\nReplace missing spaces in a string with the least frequent character:")
print("".join(series1.replace(' ', least_freq)))
