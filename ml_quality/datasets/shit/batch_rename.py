#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
pattern = re.compile(r'test\d{1,2}')

# use regular expression and folder processing to modify file names
def TravelFolders(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        # print path
        if os.path.isdir(path):
            TravelFolders(path)
        elif 'listening_passage' in path:
            print path
            m = pattern.search(path)
            if m:
                prefix = str(m.group())
                # print prefix
                head, tail = os.path.split(path)
                # print head
                # print tail
                os.rename(os.path.join(head, tail),
                          os.path.join(head, prefix + "_" + tail))

if __name__ == '__main__':
    TravelFolders(r'e:/Study/english/for my phone')
