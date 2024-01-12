from sqlalchemy import create_engine
import os
from flask import Flask, render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.abspath('videos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Add this line to import the create_engine function

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(200))
    url = Column(String(200), nullable=False)


app.config['SECRET_KEY'] = os.urandom(24)
app.config['DEBUG'] = True


@app.route('/')
def videos():
    videos = Video.query.all()
    return render_template('videos.html', videos=videos)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    app.run()
