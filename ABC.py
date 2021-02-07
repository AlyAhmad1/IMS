from flask import Flask, render_template, url_for, redirect, request, session, make_response
from flask_wtf import FlaskForm, RecaptchaField ,file
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, AnyOf
from functools import wraps
from DB import DataBase
from datetime import timedelta
import os
import sys
DB_obj = DataBase()

Application = Flask(__name__)
Application.config['SECRET_KEY'] = '!2#4%6&8(0Ali'


# making login_required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session:
            session.permanent = True
            Application.permanent_session_lifetime = timedelta(minutes=5)
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap
