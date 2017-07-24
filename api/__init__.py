#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask_restplus import Api
from app import flask_app

performance_api = Api(flask_app, prefix="/api/v1")
