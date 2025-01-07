from first_connection import index

@app.route('/player/<p>', methods = ['GET', 'POST'])
def player(p):

    get_string = None

    if p == "Roger Federer" and request.method == 'POST':
        get_string = request.form.get('string')

#       print(f"String received from form: {get_string}")

        return render_template('tournament_input.html', player = p, string = get_string)
    
    if p == "Roger Federer" and request.method == 'GET':
        return render_template('tournament_input.html', player = p)

    else:    
        return "I am " + str(p)
