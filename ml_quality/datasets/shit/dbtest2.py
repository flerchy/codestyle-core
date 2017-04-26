#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

print mdb.__file__

try:
    con = mdb.connect('localhost', 'root', '355itu11', 'test');

    cur = con.cursor()
    cur.execute("SELECT * from `user`")

    ver = cur.fetchone()
    
    # print dir(ver)
    # we always use type to reflect object's type. the below is tuple.
    # print type(ver)
    print "Database version : %s " % str(ver)
    print "Database version : {0} ".format(ver)
    
except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()