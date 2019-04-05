"""
Problem Statement : 48. How to format all the values in a dataframe as percentages?
"""
# Import numpy as np
# Import pandas as pd
import numpy as np
import pandas as pd
"""
# Initialize DataFrame 'df'
df = pd.DataFrame(np.random.random(4), columns = ['random'])

# Format the values in column 'random' of df as percentages.
out = df.style.format({'random' : '{0:.2%}'.format})

print(out)
"""
# Input
df = pd.DataFrame(np.random.random(4), columns=['random'])

# Solution
out = df.style.format({
    'random': '{0:.2%}'.format,
})
print(out)
