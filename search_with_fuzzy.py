import pandas as pd
from rapidfuzz import fuzz
from tennis_pipeline import read_csv_atp_1991_present


# Load the data
directory_path = 'tennis_atp/1991_present'
df = read_csv_atp_1991_present(directory_path)

# Define the fuzzy filter function
def fuzzy_filter_names(df, columns, name_to_match, threshold=80):
    """
    Returns a unique list of names from specified columns that fuzzy match a given name.

    Parameters:
        df (pd.DataFrame): The DataFrame to filter.
        columns (list of str): The columns to search for the name.
        name_to_match (str): The name to match against the columns.
        threshold (int): The similarity threshold (default is 80).

    Returns:
        list: A sorted, unique list of matching names.
    """
    matching_names = set()  # Use a set to ensure uniqueness
    for column in columns:
        matches = df[column].apply(lambda x: fuzz.partial_ratio(x, name_to_match) >= threshold)
        matching_names.update(df.loc[matches, column])
    return sorted(matching_names)  # Return sorted list for readability

# Player name to match
player_1 = "agssi"
threshold = 75

# Get unique names from both 'winner_name' and 'loser_name' columns
matching_names = fuzzy_filter_names(df, ['winner_name', 'loser_name'], player_1, threshold)

# Print the resulting list of names
print(matching_names)
