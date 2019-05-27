import time
import json
import tornado.ioloop
import tornado.web
import random


# new comment
def fibonacci_num(snum):
    if snum in (0, 1):
        return 1
    else:
        return fibonacci_num(snum - 1) + fibonacci_num(snum - 2)


class FibonacciHandler(tornado.web.RequestHandler):
    def get(self):
        snum = random.randint(1, 10)
        print("got request, snum={}".format(snum))
        resp = {
            'date': time.ctime(),
            'label': 'FIBONACCI',
            'sequence num': snum,
            'fibonacci': fibonacci_num(snum)
        }
        self.write(json.dumps(resp))


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hallo everyone! This is Fibonacci numbers random generator service. "
                   "To check it, visit {}fib".format(self.request.uri))


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/fib", FibonacciHandler),
        (r"/", MainHandler),
    ])
    app.listen(5555)
    print("Tornado started on port 5555")
    tornado.ioloop.IOLoop.current().start()
