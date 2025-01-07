from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test')
def test():
    return render_template('tournament_input.html')

if __name__ == "__main__":
    #run the app, #default port for flask, 5000
    app.run(host="127.0.0.1", port=5000)