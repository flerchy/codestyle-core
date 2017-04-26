#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 1.[] is true or false
import re
import sys
if []:
    print "true"
else:
    print "false"


if ['a']:
    print "true"
else:
    print "false"
# test range of for
# for x in xrange(1, 10):
#     if x % 2:
#         print str(x) + ' is odd'
#     print x

contents = [u'\n\n\u7ed9\u8fc7\u4e48\uff1f\u2026\u2026\u2026\u2026\u2026\u4eca\u5929\u770b\u5230\u4e00\u65b0\u95fb\u2026\u2018\u672a\u5a5a\u59bb\u8f66\u7978\u540e\u667a\u529b\u4ec53\u5c81 \u6218\u58eb\u67d4\u60c5\u4e0d\u6094\u7167\u987e5\u5e74\u2019\u2026\u770b\u5b8c\u95ee\u4e8c\u8d27\u7537\u53cb\uff0c\u5982\u679c\u6709\u4e00\u5929\u6211\u75f4\u5446\u4e86\uff0c\u4f60\u8fd8\u559c\u6b22\u6211\u4e0d\u2026\u7b54\u66f0\uff1a\u554a\uff1f\u75f4\u5446\uff1f\u8ddf\u4f60\u73b0\u5728\u6709\u4ec0\u4e48\u533a\u522b\u4e48\uff1f\u2026\u2026\u2026\u2026\u2026\u2026\u6709\u4ec0\u4e48\u533a\u522b\u4e48\u2026\u533a\u522b\u4e48\u2026\u522b\u4e48\u2026\u4e48\u2026\n',
            u'2015-05-15 22:31:33', u'\n']
print contents[0].encode('utf-8').strip()
# print contents[1]
# print contents[2]

arr1 = ['abc', 'def']
for i, str1 in enumerate(arr1):
    print str(i) + " " + str1

print r"%d" % (3)
str1 = r"%10d" % (2048)
str1 += chr(8) * (len(str1) + 1)
str1 = r"%10d" % (4096)
str1 += chr(8) * (len(str1) + 1)
str1 = r"%10d" % (65536)
str1 += chr(8) * (len(str1) + 1)
print str1

str1 = '<br/>'
m = re.match(r'tt<br', str1)
if m:
    print m.string


str1 = '<em>infants</em>'
pattern = re.compile(r'<\/\w+>|<\w+>')
print re.sub(pattern, ' ', str1)


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:' + str(sys.argv)
# this will be IndexError: list index out of range
# print sys.argv[1]
