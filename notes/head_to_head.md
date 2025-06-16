# head_to_head

This code is filtering a pandas DataFrame (df) to create a new DataFrame 
(head_to_head) 
that contains only the rows where the two specified players faced each other.

The filtering is using **boolean indexing** with a **compound condition**:

    ((df['player1'] == player1) & (df['player2'] == player2)) finds matches where:
        player1 is in the player1 column AND
        player2 is in the player2 column
    ((df['player1'] == player2) & (df['player2'] == player1)) finds matches where:
        The players are listed in the opposite order: player2 is in the player1 c
        olumn AND
        player1 is in the player2 column
    The | (OR) operator combines these conditions, so it captures all matches 
    between these 
    two players regardless of which one is listed first in the data.

This is commonly used in sports analytics when you have a dataset of matches 
and want to 
extract the head-to-head record between two specific players or teams. 
The resulting head_to_head DataFrame will contain all the historical matchups between these two players.