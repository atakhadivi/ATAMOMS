# Import necessary modules from sqlalchemy
from sqlalche import create_engine Column, Integer, String
from sqlalmy.ext.arative import declar_base
from sqlchemy.orm sessionmaker
fromalchemy import ForeignKey
from sqlalchemy.orm import

# Create a declarative base for defining the database tables
Base = declarative_base()

# Define the Video table with columns for video metadata and a foreign key for category
class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True)  # Unique identifier for the video
    title = Column(String)                 # Title of the video
    url = Column(String)                   # URL of the video
    thumbnail = Column(String)              # URL of the video thumbnail
    tags = Column(String)                  # Tags associated with the video
    embed = Column(String)                  # Embed code for the video
    category_id = Column(Integer, ForeignKey('category.id'))  # Foreign key for the category
    category = relationship('Category', backref='videos')  # Relationship to the Category table

# Define the Category table with columns for category metadata and a relationship to the Video table
class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)  # Unique identifier for the category
    name = Column(String)                  # Name of the category
    description = Column(String)           # Description of the category
    videos = relationship('Video', cascade='all, delete-orphan')  # Relationship to the Video table with cascade delete

# Create an engine for connecting to the SQLite database
engine = create_engine('sqlite:///videos.db')

# Create the database tables using the metadata from the declarative base
Base.metadata.create_all(engine)

# Create a session factory for creating sessions for interacting with the database
Session = sessionmaker(bind=engine)

# Create a session for interacting with the database
session = Session()

# Close the session after use
session.close()