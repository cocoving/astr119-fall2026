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
        if self.path == "/twilight":
            status = 200
            data = {"site": "lick", "type": "astronomical", "time": "test"}
        else:
            status = 404
            data = {"error": f"nothing at {self.path}"}
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)
#
#
def send_data():
    a = call_twilight
    b = call_limits

def call_twilight():
    a = twilight()

def call_limits():
    b= limits
#
#
if __name__ == "__main__":
    HTTPServer(("localhost", 8000), Handler).serve_forever()
#
#