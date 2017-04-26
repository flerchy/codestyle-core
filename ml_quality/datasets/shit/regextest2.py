#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
with open('readfile1.txt', 'r') as f:
    template = f.read()
    print template

test1 = 'RUN 000001 COMPLETED. OUTPUT IN FILE hydrogen.dat.'
pattern = re.compile(r'.+')

result1 = re.match(pattern, template)
print '******************************************'
if result1 is not None:
    print result1.group()
else:
    print 'None'
