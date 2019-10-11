from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from router import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8888)
IOLoop.instance().start()
