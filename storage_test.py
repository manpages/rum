import sys
sys.path.append('.')

import time
import calendar

from storage import *
from users   import next_token
import rumcfg as cfg

device = 'Hell-o-phone'
agreement = 'ALIESTER-666'

addAgreement(agreement, '111')
addDevice(device)

t0 = cfg.hash_sample()
setToken(agreement, device, t0)
run("""
SELECT * FROM sessions 
""")

(True, t1) = next_token(t0)
setToken(agreement, device, t1)
run("""
SELECT * FROM sessions 
""")

d = { 'device':       device
    , 'agreement':    agreement
    , 'latitude':     '45.8167'
    , 'longitude':    '15.9833'
    , 'message':      ''
    , 'beamed':       calendar.timegm(time.gmtime()) }

addCallDict(d)
run("""
SELECT * FROM calls
""")
