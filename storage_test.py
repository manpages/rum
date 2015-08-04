import sys
sys.path.append('.')

from storage import *
from users   import next_token
import rumcfg as cfg

addAgreement('ALIESTER-666', '111')
addDevice('Hell-o-phone')
t0 = cfg.hash_sample()
setToken('ALIESTER-666', 'Hell-o-phone', t0)
print(run("""
SELECT * FROM sessions 
"""))
(True, t1) = next_token(t0)
setToken('ALIESTER-666', 'Hell-o-phone', t1)
print(run("""
SELECT * FROM sessions 
"""))

print("========================")

print(run("""
SELECT * FROM agreements
"""))
print(run("""
SELECT * FROM devices
"""))
