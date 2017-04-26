#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from package1.classOne import ClassOne
# import ClassOne;
# import imp
# imp.load_source('package1.classOne','/home/gqq/MyProjects/python/packages/package1')

import sys
sys.path.append('/home/gqq/MyProjects/python/packages/package1')

from classOne import ClassOne
c1 = ClassOne();
c1.printInfo();
