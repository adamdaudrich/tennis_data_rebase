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
    #this will pass in all names in players array through that 'player' variable in the html file

    #render templates takes a template file (like an html) and processes it using Jinja templating engine. You can pass variables to the template. it helps separate the application logic from the presentation layer. You store it in 'templates' folder of your flask app. call render_template in your route function.

@app.route('/player/<p>')
def player(p):
    #Route for dynamic player pages
    if p == "Roger Federer":
        #Call a specific function from file roger_2003.py
        from roger_2003 import get_federer_matches
        
    # Get Federer match data
        federer_matches = get_federer_matches()

    # Convert the DataFrame to a list of dictionaries for rendering
        data = federer_matches.to_dict(orient='records')

    # Render the HTML template with data
        return render_template('roger_2003.html', matches=data)

    else:
        return "I am " + str(p)


#if we want to run this locally, test for development purposes
if __name__ == "__main__":
    #run the app, #default port for flask, 5000
    app.run(host="0.0.0.0", port=5000)
