from http.server import SimpleHTTPRequestHandler, HTTPServer
import logging

class S(SimpleHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Conent-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print(str(self.headers))
        self._set_response()
        self.wfile.write("GET request received".encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print(post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request received".encode('utf-8'))

def run(server_class = HTTPServer, handler_class=S, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd... on port {}'.format(port))
    httpd.serve_forever()

run()