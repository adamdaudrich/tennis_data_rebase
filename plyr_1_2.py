from tennis_pipeline import read_csv_atp_1991_present 
from rapidfuzz import fuzz 
         

directory_path = 'tennis_atp/1991_present' 
df = read_csv_atp_1991_present(directory_path)


def plyrs_and_year():

	entry_1 = input('Enter the first player\'s name : ')
	entry_2 = input('Enter the opponent\'s name : ')
	year = input('Enter the year : ')

	return entry_1, entry_2, year


def fuzzy_match(df, columns, name_to_match, threshold=80):
    """
    Returns an unique list of names from specified columns
    'columns' param is a ['list' 'of' 'columns']"

    """
    matching_names = set()  # 'set' ensures uniqueness
    for column in columns:
        matches = df[column].apply(lambda x: fuzz.partial_ratio(x, name_to_match) >= threshold)
        matching_names.update(df.loc[matches, column])
    
    sorted_names = sorted(matching_names)  # Return alphabetically sorted list 
    return sorted_names


# entry_1_matches = fuzzy_match(df, ['winner_name','loser_name'], entry_1)
# entry_2_matches = fuzzy_match(df, ['winner_name','loser_name'], entry_2)

#call the function to put variables in global scope
# plyr_1, plyr_2, year = plyrs_and_year()


# filtered_df = df[
# 	(df['tourney_date'].astype(str).str.startswith(year)) &
# 	(
# 		((df['winner_name'] == plyr_1) & (df['loser_name'] == plyr_2)) | 
# 		((df['winner_name'] == plyr_2) & (df['loser_name'] == plyr_1))
# 	)
# ]


# if not filtered_df.empty:
#     print(filtered_df.loc[:, ['tourney_name', 'tourney_date', 'winner_name', 'loser_name', 'score']])
# else:
#     print("No matches found for the specified players and year.")




