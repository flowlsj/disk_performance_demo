#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask_restplus import Resource, Namespace, fields
from api import performance_api
from performance_stat.performance import PerformanceGenerator
from performance_stat.config import Config
from flask import Request

ns = Namespace("ssd", description="SSD Performance")
performance_api.add_namespace(ns)

performance_model = performance_api.model('Performance Model', {
    'read_iops': fields.Float,
    'read_bandwith': fields.Float,
    'read_lantency': fields.Float,
    'write_iops': fields.Float,
    'write_bandwith': fields.Float,
    'write_lantency': fields.Float,
})

@ns.route("/performance")
class Performance(Resource):
    @ns.marshal_list_with(performance_model)
    def get(self):
        """
        Get performance data
        """
        raw_data = PerformanceGenerator.parseperf(Config.IOSTAT_FILE_PATH)[1:]
        resposne = dict()
        resposne["rrqmerge"] = float(raw_data[0])
        resposne["wrqmerge"] = float(raw_data[1])
        resposne["read_iops"] = float(raw_data[2])
        resposne["write_iops"] = float(raw_data[3])
        resposne["read_bandwith"] = float(raw_data[4]) / 1000
        resposne["write_bandwith"] = float(raw_data[5]) / 1000
        resposne["avgrqsz"] = float(raw_data[6])
        resposne["avgqusz"] = float(raw_data[7])
        resposne["Tlatency"] = float(raw_data[8])
        resposne["read_lantency"] = float(raw_data[9])
        resposne["write_lantency"] = float(raw_data[10])
        resposne["svctm"] = float(raw_data[11])
        resposne["util"] = float(raw_data[12])
        return resposne

    def post(self):
        """
        Modify test option
        """
        args = Request.args()
        return None
