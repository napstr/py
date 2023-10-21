# SIMPLE HTTP SERVER

import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
import sys

class iServer(BaseHTTPRequestHandler):

    def do_GET(self):
        print("Request {0}",format(self.path))
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

def getip():
    "Get the Public IP address of the  system"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    publicip = s.getsockname()[0]
    s.close()
    return publicip

ip = getip()
print("system ip ",ip)
if len(sys.argv) >= 2:
	new_port = int(sys.argv[1])
	#print("- HTTPServer Running on  http://"+ip+":8080")
else:
	new_port = int(8080)

# START SERVER :---
print("\33[30m\33[46m   - : HTTP SERVER : -  \33[0m")
print("\33[93m -  HTTP Server running on \33[4m http://{}:{} \33[0m".format(ip,new_port)) 
httpd = HTTPServer((getip(), new_port), iServer)
httpd.serve_forever()
