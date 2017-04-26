#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Peter Guan'

from db import Dict
import logging
logging.basicConfig(level=logging.INFO)

d1 = Dict()
d1["x"] = 3
print d1.x

d3 = Dict(('a', 'b', 'c'), (1, 2, 3))
print d3.b
logging.info("ok")