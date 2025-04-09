input_file_path = r'C:\Users\adamd\Documents\JEFF SACKMAN ATP\tennis_atp-master\tennis_atp-master\rebase_source\atp_matches_2003.csv'

with open(input_file_path, 'r', encoding = 'utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
    outfile.write('tourney_name, score, w_fname, w_lname, l_fname, l_lname\n')

    for line in infile:
        rows = line.strip().split(',')

        tourney_name = rows[1]
        score = rows[23]

        w_name = rows[10]
        w_name_parts = w_name.split(' ', 1)
        w_fname = w_name_parts[0]
        
        if len(w_name_parts) > 1:
            w_lname = w_name_parts[1]
        else:
            w_lname = ''

        
        l_name = rows[18]
        l_name_parts = l_name.split(' ', 1)
        l_fname = l_name_parts[0]
    
        if len(l_name_parts) > 1:
            l_lname = l_name_parts[1]
        else:
            l_lname = ''  

        if w_fname == 'Roger' and w_lname == 'Federer' and tourney_name == 'Wimbledon':
            outfile.write(f'{tourney_name},{score},{w_fname},{w_lname},{l_fname},{l_lname}\n')
            print(f'{tourney_name},{score},{w_fname},{w_lname},{l_fname},{l_lname}\n')

infile.close()
outfile.close()
