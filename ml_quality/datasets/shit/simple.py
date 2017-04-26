# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:11:33 2013

@author: Ben
"""

from __future__ import division 
import time

a = 4.56

print "Hello world %.3f"%a

    
for idx, word in zip([1,3], ['Hello', 'world!']):
    
    #check if math is true
    if not 1/2 == 0:
        print word
    print
    
print "finished at " + time.asctime(time.localtime())