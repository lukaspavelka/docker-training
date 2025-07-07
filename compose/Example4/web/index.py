#!/usr/bin/env python3
# authors: Lukas Pavelka (original Python 2 version by yeasy.github.com), updated by AI Assistant
# date: 2024-03-15

import http.server
import socketserver
import os
import socket

PORT = 8000 # Should match EXPOSE in Dockerfile and internal port in docker-compose.yml for web service

class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Get hostname for a simple unique ID
        hostname = socket.gethostname()
        # Get container's IP (can be more complex to get the "right" one if multiple interfaces)
        try:
            container_ip = socket.gethostbyname(hostname)
        except socket.gaierror:
            container_ip = "N/A"

        # A unique ID for the instance, could also use os.environ.get('HOSTNAME', 'unknown_host')
        # which is often the container ID (short form) by default in Docker.
        instance_id = os.environ.get('HOSTNAME', hostname)

        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>HAProxy Test Web Server</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f0f8ff; }}
                .container {{ background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px #cccccc; }}
                h1 {{ color: #333366; }}
                p {{ font-size: 1.1em; }}
                strong {{ color: #007bff; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello from Web Server Instance!</h1>
                <p>This request was served by:</p>
                <ul>
                    <li>Hostname: <strong>{hostname}</strong></li>
                    <li>Instance ID (HOSTNAME env var): <strong>{instance_id}</strong></li>
                    <li>Container IP (approximate): <strong>{container_ip}</strong></li>
                </ul>
                <p>If you refresh this page multiple times (and HAProxy is load balancing), you might see different instance details if multiple web server instances are running.</p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))

if __name__ == '__main__':
    # Ensure the server listens on all available interfaces within the container
    # and on the correct port.
    with socketserver.TCPServer(("0.0.0.0", PORT), SimpleHandler) as httpd:
        print(f"Serving HTTP on 0.0.0.0 port {PORT} (PID: {os.getpid()})...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.shutdown()
            httpd.server_close()
        print("Server stopped.")
