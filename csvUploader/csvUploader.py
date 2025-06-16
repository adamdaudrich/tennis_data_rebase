from flask import Flask, render_template

app = Flask(__name__)

@app.route('/csv_uploader')
def csv_uploader(): 
    return render_template('csv.html')

@app.route('/')
def index():
    return render_template('csv.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)