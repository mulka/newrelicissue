import logging

import tornado.ioloop
import tornado.web

import newrelic.agent
#newrelic.agent.initialize('newrelic.ini')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        logging.error(newrelic.agent.current_transaction())
        header = newrelic.agent.get_browser_timing_header()
        self.write("<html><head>" + header + "</head><body><body></html>")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

