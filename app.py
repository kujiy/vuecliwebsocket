import tornado.ioloop
import tornado.web
import tornado.websocket

import sched, time
import subprocess
import uuid

cl = []
s = {}
class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True  

    def open(self):
        self.id = uuid.uuid4()
        print("open=%s" % self.id)
        print(cl)
        if self not in cl:
            cl.append(self)
            s[self.id] = sched.scheduler(time.time, time.sleep)
            s[self.id].enter(2, 1, self.dostuff, ())
            s[self.id].run()

    def on_message(self, message):
        print("on_message")
        print(cl)
        for client in cl:
            client.write_message(message)

    def execute_command(self, cmd):
        # returns output as byte string
        returned_output = subprocess.check_output(cmd)

        # using decode() function to convert byte string to string
        return returned_output.decode("utf-8")

    def dostuff(self):
        cmd_output = self.execute_command(["date", '+%s'])
        self.on_message(cmd_output)
        s[self.id].enter(3, 1, self.dostuff, ())

    def on_close(self):
        print("on_closeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        scheduler.cancel(s[self.id])
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
