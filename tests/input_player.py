from flask import Flask, render_template, request
import pandas as pd
import os

file_path = "tennis_atp/atp_players.csv"
file_path = os.path.expanduser(file_path)

if os.path.exists(file_path) and os.path.isfile(file_path):
    print("CSV file successfully loaded!")
else:
    print(f"Error: File path is incorrect or the file does not exist: {file_path}")


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def input_player():

    player = None

    if request.method == 'GET':
        return render_template('input_player.html')


    elif request.method == 'POST':
        get_player = request.form.get('player')
        return render_template('input_player.html', player = get_player)

        all_player_data = pd.read_csv(file_path, encoding='utf-8') 

        #compile a regex pattern for fuzzy and case-insensitive matching
        pattern = regex.compile(f"({search_name}){{e<={max_errors}}}",regex.IGNORECASE)

        matches = []

        for _, row in all_player_data.iterrows():
            if regex.search(pattern, row['name_first']) or regex.search(pattern, row['name_last']):
                matches.append(f"{row['name_first'].capitalize()} {row['name_last'].capitalize()}")

        
        if get_player in all_player_data:



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug = True)
