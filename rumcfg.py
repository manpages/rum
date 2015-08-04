import sys
sys.path.append('.')

import hashlib
import os

def salt():
  return "tequila with salt"

def hashing_algorithm(x):
  h = hashlib.sha512(x.decode("utf-8"))
  return h.hexdigest()

def crypto_noise():
  return os.urandom(32).encode('base64')

def hash_width():
  return len(hash_sample())

def hash_sample():
  return hashing_algorithm("sample")
