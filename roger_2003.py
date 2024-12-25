from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Path to the input CSV file
input_file_path = r'~/env/tennis_1/tennis_data_rebase/tennis_atp/atp_matches_2003.csv'

def get_federer_matches():
    # Load the data
    df = pd.read_csv(input_file_path, encoding='utf-8')

    # Extract first and last names
    df[['w_fname', 'w_lname']] = df['winner_name'].str.split(' ',n=1, expand=True)
    df[['l_fname', 'l_lname']] = df['loser_name'].str.split(' ', n=1, expand=True)

    # Filter for Roger Federer's matches at Wimbledon 2003
    federer_matches = df[
        (df['w_fname'] == 'Roger') &
        (df['w_lname'] == 'Federer') &
        (df['tourney_name'] == 'Wimbledon')
    ]

    # Select required columns
    filtered_data = federer_matches[['tourney_name', 'score', 'w_fname', 'w_lname', 'l_fname', 'l_lname']]
    return filtered_data

