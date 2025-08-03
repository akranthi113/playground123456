from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

if __name__ == "__main__":
    server = HTTPServer(('', PORT), Handler)
    print(f"Serving at http://localhost:{PORT}")
    server.serve_forever()
