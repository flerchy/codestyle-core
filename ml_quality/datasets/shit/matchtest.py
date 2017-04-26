# -*- coding: utf-8 -*-
#一个简单的match实例
 
import re
# 匹配如下内容：单词+空格+单词+任意字符
m = re.search(r'(\w+) (\w+)(?P<sps>.+?)', '!!!hello world!!!')
 
print m
print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.group(1,2):", m.group(1, 2)
print m.group('sps')
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')
# print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1(?P<id>)')

str1 = 'aaa bbb ccc dddd'
list1 = str1.split()
print list1[0]

