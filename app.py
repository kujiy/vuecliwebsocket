import tornado.ioloop
import tornado.web
import tornado.websocket

import subprocess

cl = {}
 
class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def get_query_param(self, key):
        return self.get_argument(key, None, True)

    def initialize(self, key=None):
        key = self.get_query_param("key")
        if key is None:
            key=99
        self.key=key
        if self.key not in cl:
            cl[self.key] = []

    def check_origin(self, origin):  
        return True  

    def open(self):
        print("open!")
        if self not in cl[self.key]:
            cl[self.key].append(self)
        print(str(cl))

    def on_message(self, message):
        print("on_message!")
        print(str(cl))
        for client in cl[self.key]:
            client.write_message(message)
 
    def on_close(self):
        print("disconnected!")
        if self in cl[self.key]:
            cl[self.key].remove(self)
        print(str(cl))

class Cmd(tornado.web.RequestHandler):
    def get(self):
        key = self.get_argument("key", None, True)
        cmd_output = self.execute_command(["date",  '+%Y-%m-%d %H:%M:%S'])
        self.write("%s %s" % (key, cmd_output))

    def execute_command(self, cmd):
        # returns output as byte string
        returned_output = subprocess.check_output(cmd)

        # using decode() function to convert byte string to string
        return returned_output.decode("utf-8")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
 
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/websocket/cmd", Cmd),
    (r"/websocket", WebSocketHandler),
])
 
if __name__ == "__main__":
    application.listen(8081)
    tornado.ioloop.IOLoop.current().start()