After appending a DataFrame to a list using all_matches.append(head_to_head), 
all_matches becomes a list that contains DataFrame objects.
Let's say you do this multiple times:

all_matches = []
all_matches.append(head_to_head_1)  # First DataFrame
all_matches.append(head_to_head_2)  # Second DataFrame
all_matches.append(head_to_head_3)  # Third DataFrame

The resulting data structure would be:

all_matches: A Python list
Each element in the list: A complete pandas DataFrame with all its columns

So all_matches[0] would give you the first DataFrame with all its columns, all_matches[1] would give you the second DataFrame, and so on.
This pattern is commonly used when you want to collect multiple DataFrames and then later combine them, typically with: