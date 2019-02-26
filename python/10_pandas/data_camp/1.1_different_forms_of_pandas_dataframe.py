"""
Problem Statement : 1.1 Different Forms of Pandas DataFrame
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Taking 2d array as input to a DataFrame
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])

# Printing my_2darray array as a form of DataFrame
print("Printing 2d array as input to a DataFrame:")
print(pd.DataFrame(data = my_2darray[0:, 0:]))

# Taking a dictionary as input to a DataFrame
my_dict = {1 : [1, 3], 2 : [4, 2], 3 : [10, 12]}

# Printing my_dict as a form of DataFrame
print("\nPrinting a dictionary as input to a DataFrame:")
print(pd.DataFrame(my_dict))

# Taking a DataFrame as input to a DataFrame
df = pd.DataFrame(data = [4, 44, 33, 90, 10], index = range(0, 5), columns = ['Numbers'])

# Printing a DataFrame
print("\nPrinting a DataFrame as input to a DataFrame:")
print(pd.DataFrame(df))

# Taking a Series as input to a DataFrame
my_series = pd.Series({"United Kingdom" : "London", "India" : "New Delhi", "USA" : "Washington", "Belgium" : "Bressels"})

# Printing my_series as a form of DataFrame
print("\nPrinting a Series as input to a DataFrame:")
print(pd.DataFrame(my_series))
