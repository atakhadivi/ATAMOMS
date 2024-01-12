import os
from flask import Flask

app = Flask(__name__)

# Set the SECRET_KEY to a random value
app.config['SECRET_KEY'] = os.urandom(24)

# Enable debug mode
app.config['DEBUG'] = True

# Add your routes and other configurations here

if __name__ == '__main__':
    app.run()
