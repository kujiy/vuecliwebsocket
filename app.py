import tornado.ioloop
import tornado.web
import tornado.websocket
 
cl = {}
 
class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def initialize(self, key=None):
        # get query param
        key = self.get_argument("key", None, True)

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

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
 
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/websocket", WebSocketHandler),
])
 
if __name__ == "__main__":
    application.listen(8081)
    tornado.ioloop.IOLoop.current().start()