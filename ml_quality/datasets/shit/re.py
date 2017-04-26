#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import io
import re
sys.stdin = open(sys.argv[1])

# RUN 000039 COMPLETED. OUTPUT IN FILE yttrium.dat. 1 UNDERFLOW WARNING.
pattern = r'''^RUN\ 
(?P<jobnum>\d{6})\ 
COMPLETED\.\ 
OUTPUT\ 
IN\ 
FILE\ 
(?P<filename>[a-z]+\.dat)\..*$
'''
re = re.compile(pattern, re.X)

for line in sys.stdin:
    result = re.match(line)
    if result:
        print 'Job id is ' + result.group('jobnum')
        print 'File name is ' + result.group('filename')
        print ''
