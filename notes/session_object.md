# session object 

is specific to Flask. 


It's a way to store information across multiple requests from the same user.
In Flask, session is a 

#### dictionary-like object that persists data between requests. 

Here's what it does:

User-specific storage: Each user gets their own session data, identified by 
a cookie stored in their browser

Data persistence: 
The data stored in the session remains available as the user navigates through different pages or makes different requests to your application

Security: The session data is signed with a secret key so users cannot modify it

In your code example, you're:

Getting form values from a POST request (get_player1, get_player2, and get_year). Storing these values in the session
This allows you to access these values in subsequent requests/routes without needing to pass them as parameters

To use sessions in Flask, you need to:

Set a secret key for signing: app.secret_key = 'your_secret_key'
Import the session object: from flask import session

Sessions in Flask are particularly useful for:

#### User authentication (storing login status)
Storing user preferences
Maintaining state in multi-step forms
Storing temporary data that needs to persist across multiple page loads

The data is cleared when the user closes their browser or when the session expires.