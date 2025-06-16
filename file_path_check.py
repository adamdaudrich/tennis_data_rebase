import pandas as pd
import os

file_path = "tennis_atp/atp_players.csv"
file_path = os.path.expanduser(file_path)

if os.path.exists(file_path) and os.path.isfile(file_path):
    print("CSV file successfully loaded!")
else:
    print(f"Error: File path is incorrect or the file does not exist: {file_path}")


all_player_data = pd.read_csv(file_path, encoding='utf-8') 


# all_player_data['name_first'] = all_player_data['name_first'].str.lower()
# all_player_data['name_last'] = all_player_data['name_last'].str.lower()

print(all_player_data)