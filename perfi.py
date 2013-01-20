#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

from flask import Flask

import appconfig


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to perFi"


if __name__ == "__main__":
    app.debug = appconfig.DEBUG
    app.run()
