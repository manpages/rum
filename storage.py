import sys
sys.path.append('.')

import sqlite3 as s

import users

def one(q, a=()):
  db = s.connect('rum.db')
  return run(q, a, lambda x: x.fetchone())

def run(q, a=(), f=(lambda x: x.fetchall())):
  db = s.connect('rum.db')
  global db
  print("<Query>\n%s\nwith\n%s" % (q, a)) # Yeah, I know about debug. Shut up
  with db:
    e = db.cursor()
    e.execute(q, a)
    y = f(e)
    print("=> %s\n</Query>" % y)
    return y

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
  return run("""
  INSERT INTO devices (name) VALUES (?)
  """, (name,))

def addCallDict(d):
  return run("""
  INSERT INTO calls ( agreement
                    , device
                    , latitude
                    , longitude
                    , message
                    , received
                    , beamed )
  SELECT A.id                           AS agreement
       , D.id                           AS device
       , :latitude                      AS latitude
       , :longitude                     AS longitude
       , :message                       AS message
       , (SELECT strftime('%s', 'now')  AS received)
       , :beamed                        AS beamed
  FROM ( agreements AS A
       , devices    AS D )
  WHERE A.number = :agreement
    AND D.name   = :device
  """, d)

def getPasswordHash(agreement):
  return one("""
  SELECT password FROM agreements WHERE number = ?
  """, (agreement,))
