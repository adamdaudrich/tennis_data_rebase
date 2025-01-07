from flask import Flask, render_template, request, make_response
import pandas as pd
from plyr_1_2 import fuzzy_match, df

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def index_2():

    if request.method == "GET":
        result = None
        entry_1_matches = []
        entry_2_matches = []
        selected_entry_1_match = None
        selected_entry_2_match = None 
        year = None   

    if request.method == 'POST':
        #get data from the form input
        entry_1 = request.form.get('entry_1')
        entry_2 = request.form.get('entry_2')
        year = request.form.get('year')
        
        entry_1_matches = fuzzy_match(df, ['winner_name','loser_name'], entry_1)
        entry_2_matches = fuzzy_match(df, ['winner_name','loser_name'], entry_2)
        
        selected_entry_1_match = request.form.get('entry_1_match')
        selected_entry_2_match = request.form.get('entry_2_match')

        result = {
            "year": year,
            "selected_entry_1_match": selected_entry_1_match,
            "selected_entry_2_match": selected_entry_2_match
        }


#create a response object
    resp= make_response(render_template(
        'input_player.html',  
        entry_1_matches = entry_1_matches, 
        entry_2_matches = entry_2_matches,
        selected_entry_1_match=None,
        selected_entry_2_match=None,
        year=None        
    ))


    # Clear cookies for entries
    resp.set_cookie('entry_1', '', expires=0)
    resp.set_cookie('entry_2', '', expires=0)
    resp.set_cookie('year', '', expires=0)

    return resp


@app.after_request
def add_cache_control(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, public, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug = True)


# with app.app_context():
#      for rule in app.url_map.iter_rules():
#          print(f"Endpoint: {rule.endpoint}, URL: {rule.rule}")