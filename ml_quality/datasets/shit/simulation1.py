#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

xrr = np.arange(0.3, 2.4, 0.01)
vdd = 1.8
vt = 0.5
yrr = []
for x in xrr:
    y = (vdd - vt) * (1 + x - np.sqrt(x * (1 + x))) / (1 + x)
    # print y
    yrr.append(y)

# print yrr
plt.plot(xrr, yrr, 'r-')
plt.ylabel("Vq")
plt.xlabel("SR")
plt.grid(True)
plt.show()