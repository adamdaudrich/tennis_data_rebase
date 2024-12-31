from tennis_pipeline import read_csv_atp_1991_present            


directory_path = 'tennis_atp/1991_present' 
df = read_csv_atp_1991_present(directory_path)


player_1 = "Roger Federer"
player_2 = "Andre Agassi"
year = '2005'


filtered_df = df[
	(df['tourney_date'].astype(str).str.startswith(year)) &
	(
	
		((df['winner_name'] == player_1) & (df['loser_name'] == player_2)) | 
		((df['winner_name'] == player_2) & (df['loser_name'] == player_1))
	)
]

# filtered_df = df[
# ((df['winner_name'] == player_n) | 
# (df['loser_name'] == player_n) &
# df[('tourney_date')].astype(str).str.startswith(year))
# ]



# print(df.shape)print(filtered_df.info())
# print(filtered_df.info())
# pd.set_options('display.max_columns', 7)

print(filtered_df.loc[:,['tourney_date','winner_name','loser_name', 'score', 'w_ace']])


# print(filtered_df)