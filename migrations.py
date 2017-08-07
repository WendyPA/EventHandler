from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from __init__ import app

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    """user model class"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    password = db.Column(db.String(25))
    email = db.Column(db.String(30))
    def __init__(self, username,):