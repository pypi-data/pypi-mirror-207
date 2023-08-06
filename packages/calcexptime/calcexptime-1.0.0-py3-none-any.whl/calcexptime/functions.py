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



def main():
    sysargs = [eval(arg) for arg in sys.argv[1:]]
    now = datetime.now()
    d, h, m, s = get_dhms(*sysargs)
    delta = calc_expt(d, h, m, s)

    t = now + delta
    print(f'Exp. lasts: {d} days, {h} hours, {m} minutes, {s} seconds.')
    print(f'Exp. ends: {t.day}/{t.month}/{t.year} @ {t.hour}:{t.minute}:{t.second}')

if __name__ == '__main__':
    main()
