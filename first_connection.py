#import Flask object from flask
from flask import Flask, render_template
#function that comes with flask

#instatiate Flask object and assign to__ name__ variable
app = Flask(__name__)

#whenever anyone goes to our ip address (maybe with a port and slash... execute the following


@app.route('/')
def index():
    players = ['Ivan Lendl','Andre Agassi', 'Roger Federer']
    return render_template('index.html', player=players)
    #this will pass in all names in players array through 'player' variable in the html file

    #render templates takes a template file (like an html) and processes it using Jinja templating engine. You can pass variables to the template. it helps separate the application logic from the presentation layer. You store it in 'templates' folder of your flask app. 

@app.route('/player/<p>')
def player(p):
    #Route for dynamic player pages
    if p == "Roger Federer":

    # Render the HTML template with the input
        return render_template('tournament_input.hmtl', player = p)

    else:
        return "I am " + str(p)

@app.route('/federer_stats', methods=['POST'])

def federer_stats():
    tournament_name = request.form['tournament']
    federer_matches = get_federer_matches()
    filtered_data = federer_matches[federer_matches['tourney_name'].str.lower() == tournament_name.lower()]

    if not filtered_data:
        return render_template('no_data.html', tournament=tournament_name)
    
    return render_templates('roger_2003.html', matches = filtered_data, tournament=tournament_name)

#if we want to run this locally, test for development purposes
if __name__ == "__main__":
    #run the app, #default port for flask, 5000
    app.run(host="0.0.0.0", port=5000)
