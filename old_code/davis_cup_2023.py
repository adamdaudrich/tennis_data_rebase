input_file_path = r'C:\Users\adamd\Documents\JEFF SACKMAN ATP\tennis_atp-master\tennis_atp-master\rebase_source\atp_matches_2023.csv'
output_file_path = r'C:\Users\adamd\Documents\JEFF SACKMAN ATP\tennis_atp-master\tennis_atp-master\rebase_cleaned\davis_cup_2023.csv'

with open(input_file_path, 'r', encoding ='utf-8') as infile, open(output_file_path, 'w', encoding ='utf-8') as outfile:
    print(f'tournament, date, rnd, score, w_fname, w_lname, l_fname, l_lname\n')
    outfile.write(f'tournament, date, rnd, score, w_fname, w_lname, l_fname, l_lname\n')
 
    for line in infile:
        
        rows = line.strip().split(',')
        
        tourney_name = rows[1]
        t_split = tourney_name.split(' ')
        tournament = ' '.join(t_split[0:2])

        date = rows[5]
 
        year = date[:4] 
        month = date[4:6]  
        day = date[6:]  
        new_date = year + '-' + month + '-' + day

        if len(t_split) >= 4:
            rnd = t_split[3]
        else: rnd = ''
            
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
    
        if tournament == 'Davis Cup':
            print(f'{tournament},{new_date},{rnd},{score},{w_fname},{w_lname},{l_fname},{l_lname}\n')    
            outfile.write(f'{tournament},{new_date},{rnd},{score},{w_fname},{w_lname},{l_fname},{l_lname}\n')
