# boolean indexing

## pandas
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

# Filter rows where column A > 3
filtered_df = df[df['A'] > 3]

## numpy
import numpy as np

# Create an array
data = np.array([5, 10, 15, 20, 25])

# Create a boolean mask
mask = data > 15  # Returns [False, False, False, True, True]

# Use the mask to filter the array
filtered_data = data[mask]  # Returns [20, 25]

# This can be done in one step
filtered_data = data[data > 15]  # Returns [20, 25]