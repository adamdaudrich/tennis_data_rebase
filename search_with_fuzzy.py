import regex
import os
import pandas as pd

file_path = "tennis_atp/atp_players.csv"
file_path = os.path.expanduser(file_path)


if os.path.exists(file_path) and os.path.isfile(file_path):
    print("CSV file successfully loaded!")
else:
    print(f"Error: File path is incorrect or the file does not exist: {file_path}")
    
atp_players = pd.read_csv(file_path, encoding='utf-8')
print(atp_players)



def search_with_regex_fuzzy(file_path, search_name, max_errors=1):
    """
    Searches for names in a CSV file using regex with fuzzy matching.

    Parameters:
        file_path (str): Path to the CSV file.
        search_name (str): Name to search for.
        max_errors (int): Maximum allowed errors (insertions, deletions, substitutions).

    Returns:
        list: A list of matching player names (first and last).
    """

    # Load the CSV file


    return atp_players
#     # Ensure the relevant columns exist
#     if 'name_first' not in atp_players.columns or 'name_last' not in atp_players.columns:
#         raise ValueError("The CSV file must contain 'name_first' and 'name_last' columns.")

#     # Compile regex with fuzzy matching
#     pattern = regex.compile(f"({search_name}){{e<={max_errors}}}", regex.IGNORECASE)

#     # Find matches
#     matches = []
#     for _, row in atp_players.iterrows():
#         if regex.search(pattern, str(row['name_first'])) or regex.search(pattern, str(row['name_last'])):
#             matches.append(f"{row['name_first'].capitalize()} {row['name_last'].capitalize()}")

#     return matches

# search_name = "federer"
# matches = search_with_regex_fuzzy(file_path, search_name, max_errors=2)
# print(f"Matches for '{search_name}': {matches}")