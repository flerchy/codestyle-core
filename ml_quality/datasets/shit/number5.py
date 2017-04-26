#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def func1(m):
    return m.group(2).replace('an engineering', 'A science').title() + ' will be given ' + m.group(1).lower()


def func2(m):
    return m.group(2).replace('meeting', 'project') + ' on ' + m.group(1).lower() + "."

src1 = 'Tomorrow I’ll have an engineering class.'
src2 = 'The day after tomorrow I’ll have a meeting.'
p1 = re.compile(r'(\w+?) .+ (an.+ss?)')
p2 = re.compile(r'(The.+?) (I.+?)\.')
src = p1.sub(func1, src1) + '\n' + p2.sub(func2, src2).replace('I', 'We')
print src
