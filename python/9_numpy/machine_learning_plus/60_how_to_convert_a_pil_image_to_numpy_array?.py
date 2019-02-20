"""
Problem Statement : How to convert a PIL image to numpy array?
"""

# Import numpy as 'np'
import numpy as np
from io import BytesIO
from PIL import Image
import PIL, requests

# Import image from URL
URL = 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Denali_Mt_McKinley.jpg'
response = request.get(URL)

# Read it as Image
i = Image.open(BytesIO(response.content))

# Optinaly resize
i = i.resize([150, 150])

# Convert to numpy array
array = np.asarray(i)
print("PIL image to array:")
print(i)
