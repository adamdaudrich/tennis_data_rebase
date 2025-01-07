import os
import pandas as pd

def read_csv_atp_1991_present(directory_path: str):
    # List to hold all DataFrames
    data_frames = []

    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory_path, filename)
            
            # Read CSV file into DataFrame
            df = pd.read_csv(file_path)
            
            # Add the DataFrame to the list
            data_frames.append(df)
            

    # Combine all DataFrames into one (optional, depending on use case)
    combined_df = pd.concat(data_frames, ignore_index=True)
    
    return combined_df

# Example usages

# directory_path = 'tennis_atp/1991_present'  # Set your directory path here
# df = read_csv_atp_1991_present(directory_path)

# print(df.shape)
# print(df.info())
# pd.set_option('display.max_columns', 7)

# print(df.loc[[0,1],['tourney_date','winner_name','loser_name', 'score', 'w_ace']])
