#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Qiqiang Guan'

import sys
from sysConfig import SysConfig
from fileOp import FileOp
from mechines import *


class MechFactory(object):

    @staticmethod
    def create(dops):
        t = dops['-t']
        p = dops['-p']

        # print t, p
        if 'tsmc65' == t and '6m' == p:
            tp = Tsmc65_6()
        elif 'tsmc45' == t and '6m' == p:
            tp = Tsmc45_6()
        elif 'tsmc45' == t and '7m' == p:
            tp = Tsmc45_7()
        elif 'umc45' == t and '6m' == p:
            tp = Umc45_6()
        else:
            tp = None
        if tp:
            if '-g' in dops:
                tp.setgds(dops['-g'])
            if '-s' in dops:
                tp.setsch(dops['-s'])
            if '-n' in dops:
                tp.settop(dops['-n'])
            if '-r' in dops:
                tp.setrtl(dops['-r'])
            if '-d' in dops:
                tp.setdefi(dops['-d'])
            if '-v' in dops:
                tp.setpwr(dops['-v'])
        # print dir(tp)
        return tp


def main():
    lens = len(sys.argv)
    argvs = sys.argv

    # print lens
    # print argvs
    if lens == 2 and argvs[1] == '-h':
        print SysConfig.hlp
    elif lens == 2 and argvs[1] == '-c':
        FileOp.clear()
        print "clear successful!"
    elif lens >= 5 and lens % 2 == 1 and '-t' in argvs and '-p' in argvs:
        # ./code.py -t tsmc65 -p 6m
        ops = argvs[1:]
        # print ops
        dops = dict(ops[i:i + 2] for i in range(0, len(ops), 2))
        # print dops
        # factory method. create Technology and Process
        tp = MechFactory.create(dops)
        if tp:
            op = FileOp(tp)
            op.writefile()
            print "write successful, please check files"
        else:
            print "you may input error Technology or Process"
    else:
        print "input error, please check!"

if __name__ == '__main__':
    main()
