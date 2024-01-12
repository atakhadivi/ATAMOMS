from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    thumbnail = Column(String)
    tags = Column(String)
    embed = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', backref='videos')


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    videos = relationship('Video', cascade='all, delete-orphan')


engine = create_engine('sqlite:///videos.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()
