import sys
sys.path.append('.')

import tornado
import tornado.ioloop
import tornado.web
import sys

import rumcfg
import storage

class Main(tornado.web.RequestHandler):
  def get(self):
    self.set_header("Content-Type", "text/html")
    self.write("Meow?")

class Dumb(tornado.web.RequestHandler):
  def post(self):
    self.set_header("Content-Type", "application/json")
    self.write('{"result": "It fucking works", "token": "666"}')

application = tornado.web.Application([ (r"/",     Main)
                                      , (r"/dumb", Dumb) ])

if __name__ == "__main__":
  print("Listening to 10081 (sqlite: %s)" % storage.version())
  application.listen(10081)
  tornado.ioloop.IOLoop.instance().start()
