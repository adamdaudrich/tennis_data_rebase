from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Path to the input CSV file
input_file_path = r'~/venv/tennis_data_rebase_venv/tennis_data_rebase/tennis_atp/atp_matches_2003.csv'


def get_federer_matches(tournament_name=None):
    # Load the data
    df = pd.read_csv(input_file_path, encoding='utf-8')

    # Extract first and last names
    df[['w_fname', 'w_lname']] = df['winner_name'].str.split(' ',n=1, expand=True)
    df[['l_fname', 'l_lname']] = df['loser_name'].str.split(' ', n=1, expand=True)
    
    #normalize tourney_name to lowercase
    df['tourney_name'] = df['tourney_name'].str.lower()
    
    # Filters for Roger Federer's won and lost games
    federer_matches = df[
    (((df['w_fname'] == 'Roger') & (df['w_lname'] == 'Federer')) |
    ((df['l_fname'] == 'Roger') & (df['l_lname'] == 'Federer'))) ]

    # Select required columns
    filtered_matches = federer_matches[['tourney_name', 'score', 'w_fname', 'w_lname', 'l_fname', 'l_lname']]
    return filtered_matches

@app.route('/federer2003', methods=['GET', 'POST'])
def federer_2003():
    
    if request.method == 'GET':
        return redirect('/')
    
    # Handle POST
    tournament_name = request.form.get('tournament')

    federer_matches = get_federer_matches(tournament_name)
    data = federer_matches.to_dict(orient='records')
    return render_template('roger_2003.html', matches=data, tournament=tournament_name)

# if __name__ == "__main__":
# put the input into get_federer_matches function


# # if __name__ == "__main__":
#     with app.app_context():
#         for rule in app.url_map.iter_rules():
#             print(f"Endpoint: {rule.endpoint}, URL: {rule.rule}")

