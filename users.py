import sys
sys.path.append('.')

from rumcfg import *
import storage
from extras import *

def hash_password(x):
  return hashing_algorithm(hashing_algorithm(x + salt()))

def next_token(x):
  tok = hashing_algorithm(x + crypto_noise())  
  if len(x) == hash_width():
    return (True,  tok)
  return (False, "Malformed initial token. This should never happen.")

def initTokenChain(device, agreement, password):
  h = storage.getPasswordHash(agreement)
  if h is None:
    return (False, "Non-existing user")
  h = h[0]
  print(password)
  print(hash_password(password))
  print(h)
  if hash_password(password) == h:
    (tr, tok) = next_token(h)
    assrt(tr, "(initTokenChain): Token generator failure. We're very fucked!")
    storage.setToken(agreement, device, tok)
    return (True, tok)
  else:
    #inc_login_fail(agreement) # We want to eventually protect ourselves vs bruteforce
    return (False, "Wrong password.")
