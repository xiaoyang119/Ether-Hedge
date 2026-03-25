#!/usr/bin/env python3
"""Serve HedgeX DApp on localhost:8000 and auto-open browser"""
import http.server, socketserver, os, webbrowser, threading

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000
URL = f"http://localhost:{PORT}/HedgeX_DApp.html"
Handler = http.server.SimpleHTTPRequestHandler

# 1秒后自动打开浏览器
threading.Timer(1.0, lambda: webbrowser.open(URL)).start()

print(f"\n  HedgeX DApp running at: {URL}")
print(f"  Browser opening automatically...")
print(f"  Press Ctrl+C to stop\n")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
