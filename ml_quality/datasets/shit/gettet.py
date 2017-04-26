#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
# get method 
request = urllib2.Request("http://localhost:9999/lightcontroller/gett")
response = urllib2.urlopen(request)
print response.read()