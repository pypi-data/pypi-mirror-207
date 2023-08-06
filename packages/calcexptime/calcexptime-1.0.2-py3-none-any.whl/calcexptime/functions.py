#! /usr/bin/env python3

import sys
from datetime import datetime, timedelta

def get_dhms(*args):
    attr = [0, 0, 0, 0] # day, hours, minutes, seconds
    for k, arg in enumerate(args[::-1]):
        attr[k] = arg
    d, h, m, s = attr[::-1]
    return d, h, m, s

def calc_expt(d, h, m, s):
    expt = timedelta(days=d, hours=h, minutes=m, seconds=s)
    return expt

