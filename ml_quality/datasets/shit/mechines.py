#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sysConfig import SysConfig
from commonMechine2 import CommonMechine

class Tsmc45_6(CommonMechine):
    """docstring for Tsmc45_6"""
    def __init__(self):
        super(Tsmc45_6, self).__init__(SysConfig.tsmc45_6)

class Tsmc45_7(CommonMechine):
    """docstring for Tsmc45_7"""
    def __init__(self):
        super(Tsmc45_7, self).__init__(SysConfig.tsmc45_7)

class Tsmc65_6(CommonMechine):
    """docstring for Tsmc65_6"""
    def __init__(self):
        super(Tsmc65_6, self).__init__(SysConfig.tsmc65_6)

class Umc45_6(CommonMechine):
    """docstring for Umc45_6"""
    def __init__(self):
        super(Umc45_6, self).__init__(SysConfig.umc45_6)

