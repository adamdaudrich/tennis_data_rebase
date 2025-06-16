from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import os


def get_atp_names()

'''
displays a list of names from the atp_players.csv (all time)
iterates through the atp_players file to give you a fuzzy matched list of full names 
that you pick from

GET : provides the list
POST : takes in the names, splits them to first and last, and stores them in 
the flask session object

returns a list of these names

'''
    #this creates AND populates a new pandas object ie DATAFRAME
    #it does so on a per-row basis
    df = pd.read_csv("tennis_atp/atp_players.csv")
    df['name'] = df['name_first']+ ' ' + df['name_last']
    male_full_names = df['name'].tolist()

    return male_full_names



def get_year()
'''
multi select (scroll with mouse?)

takes the html input variable years
and lists them in DESCENDING order in a list

years = [2021, 1999, 1986]

2021: atp_matches_2021.csv, atp_matches_doubles_2022.csv, etc....
1999: atp_matches_199.csv, etc...
'''
    return render_template('sfdfverfer')



def get_level() 
'''
multi select

required

uses an HTML dropdown menu for variables [carpet, clay, grass, hard]
returns a CATEGORIES dataframe of these filenames


singles: atp_matches_2021.csv, atp_matches_2022.csv
doubles: atp_matches_doubles_2021.csv, atp_matches_doubles_2022.csv
futures:
challengers:


USE OS library to find substrings, pass it to the dataframe
'''

    return atp_sel_cat


def get_surfaces()
'''
'''





@app.route('/clear')
def clear_session():
    session.clear()
    return redirect(url_for('head_to_head'))



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug = True)
