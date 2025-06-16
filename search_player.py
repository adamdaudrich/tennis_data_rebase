import pandas as pd
from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'qweQWE123!@#'


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'tennis_atp')

@app.route('/search_player', methods = ['GET', 'POST'])
def search_player():
    """ 
    helper function
    To search the list you gotta use the input you're given, which is likley
    a string with a first name followed by last name
    assuming there will be spelling errors from people typing fast or on their
    phones or whatever.

    1) create a new dataframe with first name + last name merged
    hopefully the html fuzy match will be good enough
    """

    #this creates AND populates a new pandas object ie DATAFRAME
    df = pd.read_csv("tennis_atp/atp_players.csv")
    df['name'] = df['name_first']+ ' ' + df['name_last']
    all_players = df['name'].tolist()

    #handle the http requests
    if request.method == 'GET':
        return render_template('search_player.html', all_players = all_players)

    if request.method == 'POST':
        get_player1 = request.form.get('player1')
        session['player1'] = get_player1 
    
        return redirect(url_for('search_player'))



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug = True)