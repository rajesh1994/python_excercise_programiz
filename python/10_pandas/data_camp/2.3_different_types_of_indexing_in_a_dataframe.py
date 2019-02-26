"""
Problem Statement : 2.3 Different types of indexing in a pandas dataframe
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], index = [2, 'A', 4], columns = [48, 49, 50])
print("DataFrame 'df' is:")
print(df)

# Pass '2' to 'loc'
print("\nPicking elements based on DataFrame have an index labled 2:")
print(df.loc[2])

# Pass '2' to 'iloc'
print("\nPicking elements based on DataFrame that are at index 2:")
print(df.iloc[2])

# Pass '2' to 'ix'
print("\nPicking elements if your index is not solely integer-based:")
print(df.ix[2])

"""
Concept of loc and how it differs from other indexing attributes such as .iloc[] and .ix[]:

	.loc[] works on labels of your index. This means that if you give in loc[2], you look for the values of your DataFrame that have an index labeled 2.

	.iloc[] works on the positions in your index. This means that if you give in iloc[2], you look for the values of your DataFrame that are at index ’2`.

	.ix[] is a more complex case: when the index is integer-based, you pass a label to .ix[]. ix[2] then means that you’re looking in your DataFrame for values that have an index labeled 2. This is just like .loc[]! However, if your index is not solely integer-based, ix will work with positions, just like .iloc[].
"""
