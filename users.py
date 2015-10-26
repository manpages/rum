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
    storage.ensureDevice(device)
    storage.setToken(agreement, device, tok)
    return (True, tok)
  else:
    #inc_login_fail(agreement) # We want to eventually protect ourselves vs bruteforce
    return (False, "Wrong password.")

def bumpTokenChain(device, agreement, token): # ONLY TO BE CALLED AFTER AUTH!
  (tr, tok) = next_token(token)
  assrt(tr, "(bumpTokenChain): faied to generate next token from previous - " + token)
  storage.setToken(agreement, device, tok)
  return tok

def isAuthorized(device, agreement, token):
  tok = storage.getToken(agreement, device)
  if tok is None:
    return (False, "Token chain wasn't initiated, try logging in.")
  return ((token == tok[0]), "Session dropped for some reason, try logging in again.")
