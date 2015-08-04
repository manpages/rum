import sys
sys.path.append('.')

from rumcfg import *
import storage
import extras

def hash_password(x):
  return hashing_algorithm(hashing_algorithm(x + salt()))

def next_token(x):
  tok = hashing_algorithm(x + crypto_noise())  
  if len(x) == hash_width():
    return (True,  tok)
  return (False, "Malformed initial token. This should never happen.")

def init_token_chain(device, agreement, password):
  h = get_password_hash(agreement)
  if hash_password(password) == h:
    (tr, tok) = next_token(h)
    assrt(tr)
    set_token_chain((device, agreement), tok)
    return (True, tok)
  else:
    inc_login_fail(agreement)
    return (False, "Wrong password.")
