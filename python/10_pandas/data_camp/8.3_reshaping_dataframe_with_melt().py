"""
Problem Statement : 8.3 Reshaping DataFrame With melt()
"""

# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd

# Initialize 'people' DataFrame
people = pd.DataFrame({'First Name' : ['John', 'Jane'],'Last Name' : ['Doe', 'Austen'], 'Blood Type' : ['A-', 'B+'], 'Weight' : ['94', 65]})
print("The People DataFrame is:")
print(people)

# Using melt() method on the people DataFrame
print("\nReshaping the 'people' DataFrame with 'Blood Type & Weight':")
print(pd.melt(people, id_vars = ['First Name', 'Last Name'], var_name = 'measurements'))
