#!/usr/bin/env python
# -*- coding: utf-8 -*-

# some method
# tag has class property but not has id property
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
"""

soup = BeautifulSoup(html)
# print soup.prettify()

print soup.head.string
print soup.title.string
print soup.a
print soup.a.string
print type(soup.a.string)
print soup.p.string
print soup.body.string

print '################################contents###########################'
print soup.head.contents
print len(soup.head.contents)
print [str(x) for x in soup.head.contents]

print '################################child###########################'
body = soup.body.children
print body
# this code will print out u'\n'
print [x for x in soup.body.children]
for content in body:
	print content

print '################################stripped string###########################'
for string in soup.body.stripped_strings:
	print string
# 实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行
print '################################sibiling###########################'
print soup.p.next_sibling

print soup.p.prev_sibling

print soup.p.next_sibling.next_sibling
print soup.a.next_sibling.next_sibling
print '**************next_siblings****************'
for sibling in soup.a.next_siblings:
    print(repr(sibling))

print '################################findall###########################'
print soup.find_all('a')
print soup.find_all('b')
print soup.find_all('body')

print '################################method###########################'
print soup.find_all(has_class_but_no_id)

print '################################find###########################'
print soup.find('a')

