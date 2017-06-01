#!/usr/bin/env python

import pycodestyle.pycodestyle as cs
import pyparser.parser as ps
import json

import os

def main():
    indir = 'repository/'
    res = []
    style = cs.StyleGuide()
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            one_res = []
            if f.endswith(".py"):
                #print f
                fi = open(os.path.join(root, f), 'r')
                one_res.extend(ps.run(fi))
                fi.close()
                fchecker = cs.Checker(os.path.join(root, f), show_source=True)
                file_errors = fchecker.check_all()
                #print file_errors
                one_res.append({"codestyle_errors": file_errors})
                fi.close()
                res.append(one_res)
    print json.dumps(res, sort_keys=True, indent=4)
    avg = {}
    for entry in res:
        for metric in entry:
            for key in metric:
                avg[key] = 0
    for entry in res:
        for metric in entry:
            for key in metric:
                avg[key] += int(metric[key])
    for key in avg:
        avg[key] *= 1.0/len(entry)
    print avg



if __name__ == '__main__':
    main()