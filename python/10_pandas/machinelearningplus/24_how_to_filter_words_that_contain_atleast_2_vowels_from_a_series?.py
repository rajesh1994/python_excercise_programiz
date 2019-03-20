"""
Problem Statement : 24. How to filter words that contain atleast 2 vowels from a series?
"""

# Import pandas as pd
# Import Counter from collections
import pandas as pd
from collections import Counter

# Initialize series1
series1 = pd.Series(['Apple', 'Banana', 'Juice', 'Plan', 'Python', 'Money'])
print("series1:")
print(series1)

# filter words that contain atleast 2 vowels from a series
mask = series1.map(lambda x : sum([Counter(x.lower()).get(i, 0) for i in list('aeiou')]) >= 2)
print("\nFilter words that contain atleast 2 vowels from a series:")
print(series1[mask])
