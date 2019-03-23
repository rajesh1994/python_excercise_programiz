"""
Problem Statement : 42. How to replace missing values of multiple numeric columns with the mean?
"""

# Import pandas as pd
import pandas as pd

# Reading data from CSV file
df1 = pd.read_csv('cars93.csv', usecols = ['Min.Price', 'Max.Price'])
print("Data from the CSV file:")
print(df1.head(15))

# Replace missing values of multiple numeric columns with the mean
df2 = df1[['Min.Price', 'Max.Price']] = df1[['Min.Price', 'Max.Price']].apply(lambda x : x.fillna(x.mean()))
print("\nReplace missing values of multiple numeric columns with the mean:")
print(df2.head(15))

"""
pandas.DataFrame.fillna():

DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)

Parameters:
value : Static, dictionary, array, series or dataframe to fill instead of NaN.
method : Method is used if user doesn’t pass any value. Pandas has different methods like bfill, backfill or ffill which fills the place with value in the Forward index or Previous/Back respectively.
axis: axis takes int or string value for rows/columns. Input can be 0 or 1 for Integer and ‘index’ or ‘columns’ for String
inplace: It is a boolean which makes the changes in data frame itself if True.
limit : This is an integer value which specifies maximum number of consequetive forward/backward NaN value fills.
downcast : It takes a dict which specifies what dtype to downcast to which one. Like Float64 to int64.
**kwargs : Any other Keyword arguments

Return:
filled : DataFrame
"""
