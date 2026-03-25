#!/usr/bin/env python3
"""Serve HedgeX DApp on localhost:8000"""
import http.server, socketserver, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

print(f"\n  HedgeX DApp running at: http://localhost:{PORT}/HedgeX_DApp.html\n")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
