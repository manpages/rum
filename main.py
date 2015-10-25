import sys
sys.path.append('.')

import time
import calendar
from base64 import b64encode

from storage import *
from users   import next_token
import rumcfg as cfg

def main():
  device = 'Hell-o-phone'
  agreement = 'ALIESTER-666'

  addAgreement(agreement, '111')
  addDevice(device)

  t0 = cfg.hash_sample()
  setToken(agreement, device, t0)
  run("""
  SELECT * FROM sessions 
  """)

  t1 = next_token(t0)[1]
  print (t1)
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

if __name__ == "__main__":
  main()
