import http.server
import webbrowser
import os
import threading

PORT = 8000
DIR = os.path.dirname(os.path.abspath(__file__))
FILE = "HedgeX_DApp.html"

os.chdir(DIR)

def open_browser():
    webbrowser.open(f"http://localhost:{PORT}/{FILE}")

print(f"Starting server at http://localhost:{PORT}/{FILE}")
print("Press Ctrl+C to stop\n")

threading.Timer(1, open_browser).start()

http.server.HTTPServer(("", PORT), http.server.SimpleHTTPRequestHandler).serve_forever()
