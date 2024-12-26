from flask import Flask, render_template, request
import pandas as pd

#function that comes with flask
#instatiate Flask object and assign to__ name__ variable
app = Flask(__name__)

#pass players array thdo flask app.route want a function namerough 'player' variable in index.html
@app.route('/')
def index():
    players = ['Ivan Lendl','Andre Agassi', 'Roger Federer']
    return render_template('index.html', player=players)


#Route for dynamic player pages
#if federer chosen, go to tournament_input.html
@app.route('/player/<p>')
def player(p):

    if p == "Roger Federer":
        return render_template('tournament_input.html', player = p)
    else:
        return "I am " + str(p)

input_file_path = r'~/venv/tennis_data_rebase_venv/tennis_data_rebase/tennis_atp/atp_matches_2003.csv'



def get_federer_matches(str = None):
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

    
    if tournament_name:

        #Filters for Roger Federer's matches
        federer_matches = federer_matches[federer_matches['tourney_name'].str.contains(tournament_name.lower())]
        
        #select required columns
        filtered_matches = federer_matches[['tourney_name', 'score', 'w_fname', 'w_lname', 'l_fname', 'l_lname']]
        return filtered_matches


#the post comes back
@app.route('/player/Roger Federer', methods=['GET', 'POST'])

def federer_2003():
    
    if request.method == 'GET':
        return redirect('/')
    
    # Handle POST
    tournament_name = request.form.get('tournament')
    print(f"Tournament name received: {tournament_name}")


    federer_matches = get_federer_matches(tournament_name)
    data = federer_matches.to_dict(orient='records')
    return render_template('roger_2003.html', matches=data, tournament=tournament_name)


#if we want to run this locally, test for development purposes
if __name__ == "__main__":
    #run the app, #default port for flask, 5000
    app.run(host="127.0.0.1", port=5000, debug = True)


    # with app.app_context():
    #     for rule in app.url_map.iter_rules():
    #         print(f"Endpoint: {rule.endpoint}, URL: {rule.rule}")