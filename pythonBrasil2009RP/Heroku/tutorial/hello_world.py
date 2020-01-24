from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from motor import motor_tornado
import dns

client = motor_tornado.MotorClient('mongodb+srv://sysdba:masterkey@pybr-nzbn8.mongodb.net/test?retryWrites=true&w=majority')
                                    
db = client['teste']

class MainHandler(RequestHandler):
    def get(self):
        document = {'key':'value'}
        db = self.settings['db']
        db['pybr'].insert_one(document)
        self.write('E aí galera da Python Brasil 2019!')


if __name__=='__main__':
    app = Application([
                ('/', MainHandler)],
                db=db
    )
    app.listen(8000)
    IOLoop.current().start()