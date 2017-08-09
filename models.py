import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Date,Time

# from sqlalchemy import Column, Integer, String
# from app import db
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Set your classes here.


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=1)
    name = Column(String(120), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(30))
    interests = Column(String(250));
    phone = Column(String(250));



class Events(Base):
     __tablename__ = 'events'
     id = Column(Integer, primary_key=True, autoincrement=1);
     name = Column(String(80), nullable=False);
     category = Column(String(250));
     date = Column(Date);
     time = Column(Time);
     register_id = Column(Integer, ForeignKey('user.id'));
     user = relationship(User);

class Trending(Base):
    __tablename__ = 'trending'
    id = Column(Integer, primary_key=True, autoincrement=1);
    name = Column(String(80), nullable=False);
    username = Column(String(80), nullable=False)
    register_id = Column(Integer, ForeignKey('user.id'));
    user = relationship(User);

class Categories(Base):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True);
    category = Column(String(80), nullable=False, ForeignKey('user.interests'));
    user = relationship(User);


def __init__(self, name=None, password=None):
    self.name = name
    self.password = password


# Create tables.
Base.metadata.create_all(bind=engine)
