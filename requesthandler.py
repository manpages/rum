import sys
sys.path.append('.')

from storage import *
from users   import *

def handle(d):
  if d['action'] == 'login':
    return login(d)
  if d['action'] == 'heartbeat':
    return heartbeat(d)
  if d['action'] == 'call':
    return call(d)
  else:
    return unknown(d)

def login(d):
  (tr, tok) = initTokenChain(d['deviceId'], d['username'], d['password'])
  if tr:
    return { 'result': 'Token chain initialized'
           , 'token':  tok }
  else:
    return { 'error': 'Incorrect credentials' }

def heartbeat(d):
  return { 'error': 'Not implemented' }

def call(d):
  return { 'error': 'Not implemented' }

def unknown(d):
  return { 'error':  "Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn" }
