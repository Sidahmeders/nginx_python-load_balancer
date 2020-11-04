import tornado.ioloop
import tornado.web
import os
import sys

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(f"Served from {os.getpid()}")

application = tornado.web.Application([
    (r"/", MainHandler),
])

port = 8888
if __name__ == "__main__":
    if (sys.argv.__len__() > 1):
        port = sys.argv[1]

    application.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.instance().start()
