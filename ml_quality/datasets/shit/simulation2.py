#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

xrr = np.arange(0.3, 2.4, 0.01)
vdd = 2.5
vtn = 0.5
ratio = 0.5
vtp = 0.5

yrr = []
for x in xrr:
    y = (vdd - vtn) - np.sqrt(np.power(vdd - vtn, 2) - ratio * x * np.power(vdd - vtn - vtp, 2))
    # print y
    yrr.append(y)

# print yrr
plt.plot(xrr, yrr, 'r-')
plt.ylabel("Vqb")
plt.xlabel("PR")
plt.grid(True)
plt.show()
