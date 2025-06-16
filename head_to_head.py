def head_to_head(sel_atp_data)

''' 
 checks for year in filenames of a directory. This is going to encompass
ATP, Challenger, etc...

c) looks for the players names in the 'name' fields of these selected files
using the returned values from separate_names()
''' 
    h2h_matches = []
    processed_files = []
    
    try:
        for filename in os.listdir(DATA_DIR):

            # if the file matches any of the requested years and ends with .csv
            if any(year in filename for year in years) and filename.endswith('.csv'):
                
                # IF 'any' evaluates to true, the file path = the directory + the filename 
                file_path = os.path.join(DATA_DIR, filename)
                
                # set the temporay dataframe
                df = pd.read_csv(file_path)

                # IF 'any' evaluates to TRUE : add the filename (type string) to the 
                # processed_files list
                processed_files.append(filename)
                
                # AND filter the df using the pandas vectorized approach
                found_match = df[
                    ((df['player1'] == player1) & (df['player2'] == player2)) | 
                    ((df['player1'] == player2) & (df['player2'] == player1))
                ]
                
                # Add 'source_file' column to the head_to_head 
                if not found_match.empty:
                    found_match['source_file'] = filename

                #by using .append, you're appending dataframes. it is NOT
                #a single dataframe
                    h2h_matches.append(found_match)
        
        # Combine all matching data into a SINGLE dataframe
        if h2h_matches:
            result_df = pd.concat(h2h_matches, ignore_index=True)
            return result_df
        else:
            # Return empty dataframe if no matches found
            return pd.DataFrame()
            
    except Exception as e:
        print(f"Error finding head-to-head matches: {e}")
        return pd.DataFrame()


