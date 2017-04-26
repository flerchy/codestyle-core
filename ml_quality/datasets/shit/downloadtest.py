#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

url = "http://www.scientificamerican.com/podcast/podcast.mp3?fileId=0EB7C7F2-EDB5-48B5-A7630CB76CABA391&ref=sciam"

# file_name = url.split('/')[-1]
file_name = "podcast.mp3"
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 2048

while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    # print chr(8) * (len(status) + 1)
    status = status + chr(8) * (len(status) + 1)
    print status,

f.close()
