from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import twilight
import utils
import limits
import dataselector
#
#
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):

        body = json.dumps(data).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)
HTTPServer(("localhost", 8000), Handler).serve_forever()
#
#
def send_data():
    a = call_twilight
    b = call_limits

def call_twilight():
    a = twilight()

def call_limits():
    b= limits
