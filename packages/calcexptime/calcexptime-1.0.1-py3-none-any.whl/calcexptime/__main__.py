#! /usr/bin/env python3

import sys
from datetime import datetime, timedelta
from .functions import get_dhms, calc_expt

help_string = \
        f'#'*72 +'\n'+\
        f'{"CALCEXPTIME":^72s}\n\n'+\
        f'Call the program as: \n'+\
        f'$ python -m calcexptime <days> <hours> <minutes> <seconds>\n'+\
        f'#'*72 +'\n'


if len(sys.argv) == 1: # no arguments
    print(help_string)
    exit()

sysargs = [eval(arg) for arg in sys.argv[1:]]   # get the values
d, h, m, s = get_dhms(*sysargs)

now = datetime.now()    # actual date
delta = calc_expt(d, h, m, s)   # duration of the experiment

t = now + delta     # Final date

print(f'Exp. lasts: {d} days, {h} hours, {m} minutes, {s} seconds.')
print(f'Exp. ends: {t.day}/{t.month}/{t.year} @ {t.hour}:{t.minute}:{t.second}')
