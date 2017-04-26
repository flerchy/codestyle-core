#!/usr/bin/env python
# -*- coding: utf-8 -*-

def function1(arg):
    def gett(self):
        return getattr(self, '_Cm__' + arg)
    return gett

class Cm(object):

    def __init__(self):
        super(Cm, self).__init__()
        self.__top = 'a'
        self.__gds = 'b'
        # Cm.gett = classmethod(gett)
        setattr(Cm, 'gettop', function1('top'))



if __name__ == '__main__':
    cm = Cm()
    print dir(cm)

    print cm.gettop()