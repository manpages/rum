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

application = tornado.web.Application([ (r"/", Main) ])

if __name__ == "__main__":
  print("Listening to 10081 (sqlite: %s)" % storage.version())
  application.listen(10081)
  tornado.ioloop.IOLoop.instance().start()
