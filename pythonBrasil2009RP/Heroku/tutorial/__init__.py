from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

from motor import motor_tornado
from views import BaseView, RolesHandler


class MainHandler(RequestHandler):
    def get(self):
        self.write("Olá galera da Python Brasil 2019! "
                   "Para ver os rolês faça requisições para '/roles'")


def main():
    port = 8000

    client = motor_tornado.MotorClient('localhost', 27017)
    db = client.roles_db

    app = Application([
        ('/', MainHandler),
        ('/roles', RolesHandler),
       ],
       db=db
    )

    http_server = HTTPServer(app)
    http_server.listen(port)
    print('Listening on http://localhost:%i' % port)
    IOLoop.current().start()


if __name__== '__main__':
    main()
