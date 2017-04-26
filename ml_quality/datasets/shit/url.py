#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib

def decode(url):
    print urllib.unquote(url).decode('utf8').encode('utf8')

if __name__ == '__main__':
    print decode('https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=indexed+priority+queue%E6%98%AF%E4%BB%80%E4%B9%88')
    print decode("https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=%E4%B8%AD%E6%96%87%E6%90%9C%E7%B4%A2")