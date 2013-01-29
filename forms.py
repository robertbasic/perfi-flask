# -*- coding: utf-8 -*-

from wtforms import Form, TextField, PasswordField, validators


class LoginForm(Form):
    email = TextField('Email', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])
