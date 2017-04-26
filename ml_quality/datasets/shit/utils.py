#!/usr/bin/python

import math

def sigmoid(net):
    return 1.0 / (1 + pow(math.e, -1 * net))
