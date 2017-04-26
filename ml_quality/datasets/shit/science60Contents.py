#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'PETER'
import urllib
import urllib2
import re
import thread
import time
import os
from bs4 import BeautifulSoup
from os.path import expanduser
import re


class Content(object):

    subfolder = "doc_" + time.strftime('%Y%m%d') + "download/"
    home = expanduser("~")
    """docstring for content"""

    def __init__(self, filename='default.txt', url='', based='/Music/'):
        self.url = url
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.dictionary = Content.home + based + Content.subfolder

        # if directory does not exist, create a new one
        if(not os.path.exists(self.dictionary)):
            os.makedirs(self.dictionary, 0755)
        self.filename = self.dictionary + filename

    def doRequest(self):
        if(self.url == ''):
            return 'url is null'
        request = urllib2.Request(self.url, headers=self.headers)
        response = urllib2.urlopen(request)
        reads = response.read()
        soup = BeautifulSoup(reads, "lxml")
        # print soup.prettify().encode('utf-8')
        pinfo = soup.find("div", {'class': 'transcript__inner'}).findAll('p')
        print "this artcle has %d paragraphes" % len(pinfo)
        artcle = ''
        for info in pinfo:
            # print info.contents[0].encode('utf-8')
            contents = info.contents
            # print contents
            # print contents[1].string
            for content in contents:
                ce = content.encode('utf-8')
                # print 'type--------' + type(content).__name__
                print 'ce--------' + ce
                # print 'content.string------' + content.string.encode('utf-8')
                # if(type(content).__name__ == 'Tag'):
                #     print 'content.contents------' + str(content.contents).encode('utf-8')

                subartcle = ''

                # actually, content contains four types. First is just string(NavigableString)
                # Second is Tag having string, such as <a href='dd'>content</a>
                # Third is <br/>
                # Fourth is tag without string, such as <a>sdfdsf<em>ddd</em>ttt</a>
                typename = type(content).__name__
                if(typename == 'NavigableString'):
                    print '1 p'
                    subartcle = content.string.encode('utf-8')
                else:
                    # if content is Tag
                    if content.string:
                        print '2 p'
                        subartcle = content.string.encode('utf-8')
                    elif re.match(r'<br', ce):
                        print '3 p'
                        subartcle = ''
                    else:
                        print '4 p'
                        pattern = re.compile(r'<\/\w+>|<\w+>')
                        # replace http tag as ''
                        for subcontent in content.contents:
                            encodesubcontent = subcontent.encode('utf-8')
                            subartcle += re.sub(pattern, '', encodesubcontent)

                artcle += subartcle
            # change a new line when a paragraph end
            artcle += "\n\n"
        return artcle

    def writefile(self, contents):
        f = open(self.filename, 'w')
        f.write(contents)
        f.close()

    def start(self):
        artcle = self.doRequest()
        self.writefile(artcle)
        # print 'ok'


# c = Content('latex-lining-could-quiet-plane-rides.txt', 'http://www.scientificamerican.com/podcast/episode/infants-already-glued-to-multiple-screens1/')
# c = Content('http://www.scientificamerican.com/podcast/episode/seashell-shapes-show-strength-for-safety1/', 'seashell-shapes-show-strength-for-safety1.txt')

# c.start()
