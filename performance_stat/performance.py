#!/usr/bin/python
# -*- coding:utf-8 -*-

import commands as syscommands

class PerformanceGenerator(object):
    '''
    Class for performance parse and generate
    '''
    @classmethod
    def __getperf(cls, filepath):
        command = 'cat ' + filepath + "| grep -i nvme0 | tail -n 3"
        res = PerformanceGenerator.__commandsRawContent(command)
        if res is not None:
            return res
        return None

    @classmethod
    def __commandsRawContent(cls, command):
        res = syscommands.getstatusoutput(command)
        if res[0] != 0:
            return None
        return res[1]

    @classmethod
    def parseperf(cls, filepath):
        res = PerformanceGenerator.__getperf(filepath)
        if res is not None:
            ressplit = res.split("\n")[0]
            return ressplit.split()
        else:
            return [0, 0, 0]