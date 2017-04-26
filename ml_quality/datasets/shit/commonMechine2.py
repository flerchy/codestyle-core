#!/usr/bin/env python
# -*- coding: utf-8 -*-


def getGenerator(key):
    def gett(self):
        return getattr(self, "__" + key)
    return gett


def setGenerator(key):
    def sett(self, val):
        return setattr(self, "__" + key, val)
    return sett


class CommonMechine(object):

    def __init__(self, dicConfig):
        super(CommonMechine, self).__init__()
        self.keys = ('lef', 'lib', 'sdc', 'drc', 'lvs',
                     'synthesis', 'top', 'gds', 'sch', 'defi', 'rtl', 'pwr')
        for key in self.keys:
            setattr(CommonMechine, "__" + key, dicConfig[key])
            setattr(CommonMechine, "get" + key, getGenerator(key))
            setattr(CommonMechine, "set" + key, setGenerator(key))
