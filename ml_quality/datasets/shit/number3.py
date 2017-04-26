#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import io
import re
sys.stdin = open(sys.argv[1])

pattern = "Fred"
regexp = re.compile(pattern)

for line in sys.stdin:
    result = regexp.search(line)
    if result:
        sys.stdout.write(line)
