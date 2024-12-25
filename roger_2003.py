from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Path to the input CSV file
input_file_path = r'~/env/tennis_1/tennis_data_rebase/tennis_atp/atp_matches_2003.csv'

def get_federer_matches(tournament_name=None):
    # Load the data
    df = pd.read_csv(input_file_path, encoding='utf-8')

    # Extract first and last names
    df[['w_fname', 'w_lname']] = df['winner_name'].str.split(' ',n=1, expand=True)
    df[['l_fname', 'l_lname']] = df['loser_name'].str.split(' ', n=1, expand=True)

    # Filters for Roger Federer's won and lost games
    federer_matches = df[
        (df['w_fname'] == 'Roger') &
        (df['w_lname'] == 'Federer') &
        (df['l_fname'] == 'Roger') &
        (df['w_lname'] == 'Federer')
    ]
    
    # 
    if tournament_name:
        federer_matches = federer_matches['tourney_name'].str.lower() == tournament_name.lower()
    ]

    # Select required columns
    filtered_data = federer_matches[['tourney_name', 'score', 'w_fname', 'w_lname', 'l_fname', 'l_lname']]
    return filtered_data


@app.route('/roger-2003', methods=['GET', 'POST'])
def federer_2003_data():
    if request.method == 'POST':
        # Get the tournament name from the form
        tournament_name = request.form.get('tournament')
        # Fetch Roger Federer's matches for the selected tournament
        federer_matches = get_federer_matches(tournament_name)
        # Convert DataFrame to a list of dictionaries for rendering
        data = federer_matches.to_dict(orient='records')
        return render_template('roger_2003.html', matches=data, tournament=tournament_name)
    
