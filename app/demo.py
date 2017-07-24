#!/usr/bin/python
# -*- coding:utf-8 -*-

from app import flask_app
from flask import render_template

@flask_app.route('/index')
def index():
    return render_template("index.html")
