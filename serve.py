#!/usr/bin/env python3
"""Serve the dataset web view. Usage: python3 serve.py [port]"""
import http.server
import os
import socket
import sys
import threading
import webbrowser

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *args):
        pass


class Server(http.server.ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True


class Server6(Server):
    address_family = socket.AF_INET6


# "localhost" can resolve to IPv4 or IPv6 (VS Code port forwarding may use either), so listen on both.
servers = [Server(("127.0.0.1", PORT), NoCacheHandler)]
try:
    servers.append(Server6(("::1", PORT), NoCacheHandler))
except OSError:
    pass
for s in servers[1:]:
    threading.Thread(target=s.serve_forever, daemon=True).start()

url = f"http://localhost:{PORT}/"
print(f"Serving {url}  (Ctrl+C to stop). Edit the CSV files; the page updates in 2 seconds.")
webbrowser.open(url)
try:
    servers[0].serve_forever()
except KeyboardInterrupt:
    pass
