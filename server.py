import SimpleHTTPServer
import SocketServer
import logging
import cgi
from io import BytesIO
import time


PORT = 5000

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(body)
        millis = int(round(time.time() * 1000))
        print (response.getvalue() + '&' + "time=" + str(millis/3600000)+'\n')
        f= open("/Users/pavan/Desktop/Research/Masters_Project/SRC/assessments/assess1_LP.txt",'a+')
        f.write(response.getvalue() + '&' + "time=" + str(millis/3600000)+'\n')
        f.close()
        

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "At port", PORT
httpd.serve_forever()