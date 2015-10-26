import sys
sys.path.append('.')

import json
import tornado
import tornado.ioloop
import tornado.web
import sys

import rumcfg
import storage
from requesthandler import handle

class Main(tornado.web.RequestHandler):
  def get(self):
    self.set_header("Content-Type", "text/html")
    self.write("Meow?")

class Dumb(tornado.web.RequestHandler):
  def post(self):
    self.set_header("Content-Type", "application/json")
    try:
      x = self.request.body
      k = x.rfind('}')
      c = lambda x: "Got request ``" + x + "''"
      d = json.loads(x[:(k+1)])

      print(c(x))
    except:
      self.write('{"error": "Malformed request"}such padded much random')
      return
    y = json.dumps(handle(d))
    print("Woohoo ``" + y + "''")
    self.write(y)
    return

application = tornado.web.Application([ (r"/",     Main)
                                      , (r"/dumb", Dumb) ])

if __name__ == "__main__":
  print("Listening to 10081 (sqlite: %s)" % storage.version())
  application.listen(10081)
  tornado.ioloop.IOLoop.instance().start()
