from __init__ import app
from app import Login
from flask_wtf import form
from flask import flash
from flask_login import login_user

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/login', methods=['GET','POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        login_user(user)
        flash('logged in successfully')