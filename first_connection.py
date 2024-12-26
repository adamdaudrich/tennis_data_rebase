from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)

#pass players array to flask app.route want a function namerough 'player' variable in index.html
@app.route('/')
def index():
    players = ['Ivan Lendl','Andre Agassi', 'Roger Federer']
    return render_template('index.html', player=players)


@app.route('/player/<p>', methods = ['GET', 'POST'])
def player(p):

    get_string = None


    if request.method == 'POST':
        get_string = request.form.get('string')
        print(f"String received from form: {get_string}")
        return render_template('tournament_input.html', player = p, string = get_string)
    
    elif request.method == 'GET':
        return render_template('tournament_input.html', player = p)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug = True)


    # with app.app_context():
    #     for rule in app.url_map.iter_rules():
    #         print(f"Endpoint: {rule.endpoint}, URL: {rule.rule}")