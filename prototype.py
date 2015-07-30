import sys
sys.path.append('.')

import tornado
import tornado.ioloop
import tornado.web
import sys

import rumcfg

class Main(tornado.web.RequestHandler):
  def get(self):
    self.set_header("Content-Type", "text/html")
    self.write("1337")

application = tornado.web.Application([ (r"/", Main) ])

if __name__ == "__main__":
  print("Listening to 8894")
  application.listen(8894)
  tornado.ioloop.IOLoop.instance().start()
