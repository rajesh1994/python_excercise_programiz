"""
Problem Statement : 60. How to create a new column that contains the row number of nearest column by euclidean distance?
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize DataFrame 'df'
df = pd.DataFrame(np.random.randint(1, 100, 40).reshape(10, -1), columns = list('pqrs'), index = list('abcdefghij'))
print("DataFrame 'df':")
print(df)

# Initialize outputs
nearest_rows = []
nearest_distance = []

# Iterate rows
for i, row in df.iterrows():
	curr = row
	rest = df.drop(i)
	# Initialize dict to store euclidean distance for current row
	e_dists = {}
	# Iterate the rest of the rows for current row
	for j, contestant in rest.iterrows():
		# Compute euclidean distance & update e_dists
		e_dists.update({j : round(np.linalg.norm(curr.values - contestant.values))})
	# Update the nearest row to the current row & the distance value
	nearest_rows.append(max(e_dists, key = e_dists.get))
	nearest_distance.append(max(e_dists.values()))
df['nearest_rows'] = nearest_rows
df['nearest_distance'] = nearest_distance
print("\nEach row contains the row number of nearest row-record by euclidean distance:")
print(df)
