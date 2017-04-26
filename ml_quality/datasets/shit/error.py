import urllib2
 
requset = urllib2.Request('http://www.baidududu.com')
try:
    urllib2.urlopen(requset)
    print "requset ok"
except urllib2.HTTPError, e:
	print "HTTPError"
	print e.code
	print e.reason
except urllib2.URLError, e:
	print "URLError"
	print e.reason
    # print e.code

print ""
req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason