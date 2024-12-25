from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Tennisdatarebase1!@127.0.0.1:3306/testDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Test the connection
try:
    with app.app_context():
        db.session.execute(text('SELECT 1'))  # A simple query to test the connection
    print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")

