import sys
sys.path.append('.')

import sqlite3 as s

import users

db = s.connect('rum.db')

def one(q, a=()):
  return run(q, a, lambda x: x.fetchone())

def run(q, a=(), f=(lambda x: x.fetchall())):
  global db
  print("Running: %s with %s" % (q, a))
  with db:
    e = db.cursor()
    e.execute(q, a)
    return f(e)

def version():
  return one('SELECT SQLITE_VERSION()')

def addAgreement(agreement, password):
  return run("""
  INSERT INTO agreements ( number
                         , password )
  VALUES ( ?, ? )
  """, (agreement, users.hash_password(password)))

def getToken(agreement, device):
  return one("""
  SELECT token FROM sessions
  WHERE agreement = (SELECT id FROM agreements WHERE number = ?)
    AND device    = (SELECT id FROM devices    WHERE name   = ?)
  """, (agreement, device))

def setToken(agreement, device, token):
  return run("""
  INSERT OR REPLACE INTO sessions
  SELECT A.id AS agreement
       , D.id AS device
       , ?    AS token
  FROM agreements AS A
     , devices    AS D
  WHERE A.number = ?
    AND D.name   = ?
  """, (token, agreement, device))

def addDevice(name):
  print (name)
  return run("""
  INSERT INTO devices (name) VALUES (?)
  """, (name,))
