import tornado
from tornado import autoreload
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from router import app

sockets = tornado.netutil.bind_sockets(port=80, backlog=256)
tornado.process.fork_processes(0)
server = HTTPServer(WSGIContainer(app))
server.add_sockets(sockets)
ioloop = IOLoop.instance()
autoreload.start(ioloop)
ioloop.start()
