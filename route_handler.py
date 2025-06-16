from flask import Flask, render_template, request, redirect, 
url_for, session

app = Flask(__name__)
app.secret_key = 'qweQWE123!@#'
#app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)


@app.route('/', methods=['GET','POST'])
def data_handler():

    #[assign male_full_names to the front end
    if request.method == 'GET':
        return render_template('splash.html', atpFullNames = atp_full_names, 
        atpPlyrs = atp_plyrs, atpYears = atp_years, atpLvl = atp_lvl, 
        atpSurface = atp_surface)

    # set entered string into the session object for persistence across session
    if request.method == 'POST':

        get_atp_plyrs = request.form.getlist('atpPlyrs[]')
        get_atp_years = request.form.getlist('atpYears[]')
        get_atp_lvl = request.form.getlist('leVel[]')
        get_atp_surface = request.form.getlist('surFace[]')

        session['players'] = get_atp_plyrs
        session['years'] = get_atp_years
        session['level'] = get_atp_lvl
        session['surface'] = get_atp_surface
    
        return redirect(url_for('return_data'))


        sel_atp_plyrs = session.get('players')
        sel_atp_years = session.get('years')
        sel_atp_lvl = session.get('level')
        sel_atp_surfaces = session.get('surfaces')

        sel_atp_data = None

    if sel_atp_plyr and sel_atp_years and sel_atp_lvl and sel_atp_surface:
        #call the function that builds sel_atp_data 
        #and sends to the html displays it

    return render_template('return_data.html')
    htmlVar1 = python_variable1, 2, 3, 4, 5, 6, 7)

app.route
def show_data



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug = True)

    