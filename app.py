
from flask_wtf import Form
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Email

class Login(Form):
    """login form with username, password fields and submit btn"""
    username = StringField('Enter your UserName', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(message='Please enter your password')])
    remember_me = BooleanField('Keep me logged in')
    login = SubmitField('Log In')