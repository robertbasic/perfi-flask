#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

from flask import Flask, request, render_template, session, url_for, flash,\
                    redirect

from function_decorators import login_required, redirect_if_logged_in
from forms import LoginForm
import appconfig


app = Flask(__name__)


@app.route("/")
@login_required
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
@redirect_if_logged_in
def login():
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate():
        email = form.email.data
        password = form.password.data

        # TODO: needs proper login here
        if email == "test@perfi.local" and password == "test":
            session['logged_in'] = True
            flash("Logged in!")
            return redirect(url_for("index"))

    return render_template('login.html', form=form)

@app.route('/logout/')
@login_required
def logout():
    session.pop('logged_in', None)
    flash("Logged out!")
    return redirect(url_for('login'))


def setup(app):
    app.debug = appconfig.DEBUG
    app.secret_key = appconfig.SESSION_SECRET_KEY

if __name__ == "__main__":
    app.run()
    setup(app)
