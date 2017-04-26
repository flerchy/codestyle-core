#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup


def has_class_but_no_id(tag):
    # return tag.has_attr('class') and not tag.has_attr('id')
    pass


def read_unicode(text, charset='utf-8'):
    if isinstance(text, basestring):
        if not isinstance(text, unicode):
            text = unicode(obj, charset)
    return text


page = 2
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    reads = response.read()
    soup = BeautifulSoup(reads, "lxml")
    # print soup.prettify().encode('ascii', 'ignore')
    # print repr(soup.title.string)
    # content = soup.select('.article')
    # content = soup.select('.article .block .untagged .mb15')
    content2 = soup.findAll('div', {'class': 'article block untagged mb15'})
    print len(content2)
    # print content2
    # content3 = content2.findAll('div',{'class':'content'})
    i = 0
    for divContent in content2:
        img = divContent.findAll('div', class_='thumb')
        # print str(i) + ' ' + str(len(img))
        # print "***************************************************"
        i = i + 1
        # will found info without img
        # if not img:
        #     qiubais = divContent.findAll('div', class_='content')
        #     for qiubai in qiubais:
        #         contents = qiubai.contents
        # strip用来清除空格回车什么的
        #         print contents[0].encode('utf-8').strip()
        # for con in contents:
        #     print read_unicode(str(con))
        # print qiubai.string
        # print BeautifulSoup(str(qiubai)).div.content
        # print BeautifulSoup(qiubai).div.string
        # print qiubai
        # print content2[0].select(".content")
        if not img:
            print "**************** start **************************"
            print divContent.find('div', class_='content').contents[0].encode('utf-8').strip()
            print "**************** end **************************\n"

    # print content3
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
