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


# making login_required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap
