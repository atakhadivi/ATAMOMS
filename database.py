from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    thumbnail = Column(String)
    tags = Column(String)
    embed = Column(String)


engine = create_engine('sqlite:///videos.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()
