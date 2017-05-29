#!/usr/bin/env python

import pycodestyle.pycodestyle as cs
import pyparser.parser as ps

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
                one_res.append(ps.run(fi))
                fi.close()
                fchecker = cs.Checker(os.path.join(root, f), show_source=True)
                file_errors = fchecker.check_all()
                one_res.append({"codestyle_errors": file_errors})
                fi.close()
                res.append(one_res)
    print res


if __name__ == '__main__':
    main()