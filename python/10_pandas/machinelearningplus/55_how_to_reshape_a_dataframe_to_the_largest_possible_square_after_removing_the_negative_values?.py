"""
Problem Statement : 55. How to reshape a dataframe to the largest possible square after removing the negative values?
"""
# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10, -1))
print("DataFrame 'df' is:")
print(df)

# Step 1 : Remove negative values from DataFrame
df1 = df[df > 0].values.flatten()
#print(df1)
df2 = df1[~np.isnan(df1)]
#print(df2)

# Step 2 : find side-length of largest possible square
n = int(np.floor(df2.shape[0] ** .5))

# Step 3: Take top n^2 items without changing positions
top_indexes = np.argsort(df2)[::-1]
output = np.take(df2, sorted(top_indexes[:n ** 2])).reshape(n, -1)
print("\nLargest possible square after removing the negative values:")
print(pd.DataFrame(output))
