#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'PETER'

import urllib2
import time
import os
from os.path import expanduser
import sys


class DownloadFile(object):

    home = expanduser("~")
    subfolder = time.strftime('%Y%m%d') + "download/"

    def __init__(self, filename, url, based='/Music/'):
        self.dictionary = DownloadFile.home + based + DownloadFile.subfolder
        # self.dictionary = based + DownloadFile.subfolder
        # if directory does not exist, create a new one
        if(not os.path.exists(self.dictionary)):
            os.makedirs(self.dictionary, 0755)
        self.filename = self.dictionary + filename
        self.url = url

    def doDownload(self):
        u = urllib2.urlopen(self.url)
        f = open(self.filename, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (self.filename, file_size)

        file_size_dl = 0
        block_sz = 2048

        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            # delete output every time, add new progress
            status = status + chr(8) * (len(status) + 1)
            print status,
        f.close()
        print('\n')

    def start(self):
        self.doDownload()

# download = DownloadFile('p.mp3', "http://www.scientificamerican.com/podcast/podcast.mp3?fileId=0EB7C7F2-EDB5-48B5-A7630CB76CABA391&ref=sciam")
# download.start()
