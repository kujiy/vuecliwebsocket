import tornado.ioloop
import tornado.web
import tornado.websocket

import subprocess

import threading
import shlex
import time
import re


import tornado.ioloop
import tornado.web
from tornado import gen
import asyncio

cl = {}
thread = {}
thread_stop = {}


class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def get_query_param(self, key):
        return self.get_argument(key, None, True)

    def initialize(self, key=None):
        self.output = "init"

        key = self.get_query_param("key")
        if key is None:
            key=99
        self.key=key

        if self.key not in cl:
            cl[self.key] = []
            print("run!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            self.run()

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
            client.write_message(self.output)
 
    def on_close(self):
        print("disconnected!")
        if self in cl[self.key]:
            cl[self.key].remove(self)
        if len(cl) == 0:
            self.stop()
        print(str(cl))

    def start_thread(self):
        while True:
            print('thread writeLogning')
            self.run_command()
            if thread_stop[self.key]:
                break

    def run_command(self):
        command = "top"
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        while True:
            output = process.stdout.readline().strip().decode("utf-8") + "\n"
            if re.match("Processes.*", output):
                self.on_message(self.key)
                self.output = ""
                time.sleep(10)
            if output == '' and process.poll() is not None:
                break
            if output:
                # print(output.strip())
                self.output += output
        rc = process.poll()
        return rc

    def run(self):
        thread_stop[self.key] = False
        thread[self.key] = threading.Thread(target=self.start_thread)
        thread[self.key].start()

    def stop(self):
        thread_stop[self.key] = True
        thread[self.key].join()
        print('thread killed')

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