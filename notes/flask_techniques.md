Multiple buttons in the same form - The browser will send the name/value of the button that was clicked:
<form action="/process" method="post">
    <input type="text" name="player" value="Roger Federer">
    <button type="submit" name="action" value="save">Save Player</button>
    <button type="submit" name="action" value="compare">Compare Player</button>
  </form>

  @app.route('/process', methods=['POST'])
def process():
    player = request.form.get('player')
    action = request.form.get('action')
    
    if action == 'save':
        # Save logic
    elif action == 'compare':
        # Compare logic

@app.route('/player_management', methods=['GET', 'POST'])
def player_management():
    # For GET requests, just display the page
    if request.method == 'GET':
        all_players = get_all_players()  # Helper function
        return render_template('player_page.html', players=all_players)
    
    # For POST requests, check which action was requested
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'add':
            player_name = request.form.get('player_name')
            add_player_to_session(player_name)  # Helper function
            
        elif action == 'remove':
            player_id = request.form.get('player_id')
            remove_player_from_session(player_id)  # Helper function
            
        elif action == 'compare':
            player_ids = request.form.getlist('player_ids')
            return redirect(url_for('show_comparison', ids=','.join(player_ids)))
        
        # After processing, redirect back to the same page (for a fresh GET request)
        return redirect(url_for('player_management'))