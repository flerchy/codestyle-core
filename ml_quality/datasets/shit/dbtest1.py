#!/usr/bin/python
# -*- coding: utf-8 -*-

import _mysql
import sys

print _mysql.__file__
# print sys.__file__
import os
path = os.path.dirname(_mysql.__file__)
print path

try:
    con = _mysql.connect('localhost', 'root', '355itu11', 'test')
        
    con.query("SELECT VERSION()")
    result = con.use_result()
    
    print "MySQL version: %s" % \
        result.fetch_row()[0]
    
except _mysql.Error, e:
  
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    
    if con:
        con.close()