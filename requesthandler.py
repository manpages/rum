import sys
sys.path.append('.')

import time
import calendar

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
  def callDo(d):
    lon = d['payload']['position']['coords']['longitude']
    lat = d['payload']['position']['coords']['latitude']
    d1 = { 'device':        d['deviceId']
         , 'agreement':     d['username']
         , 'latitude':      lat
         , 'longitude':     lon
         , 'message':       ''
         , 'beamed':        calendar.timegm(time.gmtime()) }
    c = storage.addCallDict(d1)
    return { 'result': 'Call #' + str(c) + ' accepted'
           , 'token':   bumpTokenChain(d['deviceId'], d['username'], d['token']) }
  (tr, msg) = isAuthorized(d['deviceId'], d['username'], d['token'])
  if tr:
    return callDo(d)
  else:
    return { 'error': msg }

def unknown(d):
  return { 'error':  "Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn" }
