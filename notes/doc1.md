'''
BASIC DESIGN:
each helper function returns the desired data item (category, year, player)
and populates a pandas dataframe, which, with each subsequent POST request, is
updated with the new info the user wants

We're esssentially building a data frame that looks like

df
[categories]
[years][2021]: atp_matches_doubles_2021.csv, etc
       [1999]: 
[players][singles]
         [doubles]
[tournaments][USOpen]
             [Roland_Garros]
[surfaces][clay]
         [hard]
         [carpet]

so that you can type in for example two players and look at their head-to-head
match data over several years and on chosen surfaces

'''
#------------------------------------------------------------------------------