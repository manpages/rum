import sys
sys.path.append('.')

from base64 import b64encode

import hashlib
import os

def salt():
  return "tequila with salt"

def hashing_algorithm(x):
  h = hashlib.sha512(x.encode())
  return h.hexdigest()

def crypto_noise():
  x = os.urandom(32)
  return str(x)

def hash_width():
  return len(hash_sample())

def hash_sample():
  return hashing_algorithm("sample")
