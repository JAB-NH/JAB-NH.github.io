import http.server
import socketserver
import os

PORT = 8090
DIRECTORY = r"c:\Users\j-a-b\.gemini\antigravity\scratch\google_site"

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with ThreadedHTTPServer(("0.0.0.0", PORT), QuietHandler) as httpd:
        httpd.serve_forever()
