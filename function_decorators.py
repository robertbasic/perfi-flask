# -*- coding: utf-8 -*-


from functools import wraps
from flask import session, g, redirect, url_for, flash


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash("You need to log in to proceed!")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def redirect_if_logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('logged_in'):
            flash("You are already logged in!")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function
