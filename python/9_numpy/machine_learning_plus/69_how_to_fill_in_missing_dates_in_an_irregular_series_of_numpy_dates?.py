"""
Problem Statement : How to fill in missing dates in an irregular series of numpy dates?
"""

# Import numpy as 'np'
import numpy as np

# Initialize an array 'date':
dates = np.arange(np.datetime64('2001-01-01'), np.datetime64('2001-01-09'), 2)
print("Array 'date' is:")
print(dates)

# Method 1: For loop
output1 = []
for date, difference in zip(dates, np.diff(dates)):
    output1.append(np.arange(date, (date + difference)))
filled_in1 = np.array(output1).reshape(-1)
print("\nFor loop version:\nMissing dates:")
print(filled_in1)

# Method 2: List Comprehension
filled_in2 = np.array([np.arange(date, (date + difference)) for date, difference in zip(dates, np.diff(dates))]).reshape(-1)
output2 = np.hstack([filled_in2, dates[-1]])
print("\nList comprehension version:\nMissing dates:")
print(output2)
