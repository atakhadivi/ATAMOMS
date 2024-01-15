from sqlalchemy import create_engine
import os
from flask import Flask, render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Initialize Flask app
app = Flask(__name__)

# Configure the SQLite database URI and enable debug mode
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.abspath('videos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)
app.config['DEBUG'] = True

# Create the SQLAlchemy engine and bind it to the Flask app
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
db_session = scoped_session(sessionmaker(bind=engine))

# Initialize the declarative base for SQLAlchemy models
Base = declarative_base()

# Define the Video model for the SQLite database


class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(200))
    url = Column(String(200), nullable=False)

# Define the route for the homepage, which queries all videos from the database


@app.route('/')
def videos():
    videos = Video.query.all()
    return render_template('index.html', videos=videos)

# Define the route for a specific video, which queries the video by its ID


@app.route('/video/<int:video_id>')
def video(video_id):
    video = Video.query.get_or_404(video_id)
    return render_template('video.html', video=video)

# Define the teardown function to remove the database session when the app is closed


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# Run the Flask app
if __name__ == '__main__':
    # Create the database tables if they don't exist
    Base.metadata.create_all(bind=engine)
    app.run()
