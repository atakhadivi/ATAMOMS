import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videos.db'
db = SQLAlchemy(app)

# Set the SECRET_KEY to a random value
app.config['SECRET_KEY'] = os.urandom(24)

# Enable debug mode
app.config['DEBUG'] = True

# Add your routes and other configurations here

if __name__ == '__main__':
    app.run()
