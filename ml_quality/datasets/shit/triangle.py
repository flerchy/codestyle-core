#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def get_side_len(base, height):
    if base <= 0 or height <= 0:
        return 0
    return math.sqrt(base * base + height * height)

print get_side_len(3, 4)
