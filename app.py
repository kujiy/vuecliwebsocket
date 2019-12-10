import tornado.ioloop
import tornado.web
import tornado.websocket
 
cl = []
 
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):  
        return True  

    def open(self):
        if self not in cl:
            cl.append(self)
 
    def on_message(self, message):
        for client in cl:
            client.write_message(message)
 
    def on_close(self):
        if self in cl:
            cl.remove(self)
 
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