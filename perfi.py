#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

from flask import Flask, render_template

import appconfig


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = appconfig.DEBUG
    app.run()
