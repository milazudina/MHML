from http.server import SimpleHTTPRequestHandler, HTTPServer
#from keras.models import model_from_json
#from keras.models import load_model
import load_model
import logging

reqcount = 0
probs = 0

# This class handles any incoming requests
class S(SimpleHTTPRequestHandler):
    
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

# Handles the GET requests
    def do_GET(self):
        print(str(self.headers).split()[1])
        
        keyword = str(self.headers).split()[1] 
        
        if (keyword in "getClassifier"):
            return
        self._set_response()
        global reqcount
        global probs
        self.wfile.write(str(reqcount).encode('utf-8'))
        print(probs)
        reqcount = 0

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        
        print(post_data.decode('utf-8'))
        self._set_response()
        global reqcount
        global probs
        reqcount+=1
        probs = printstuff(reqcount)
        
        self.wfile.write("POST request received".encode('utf-8'))


def run(server_class = HTTPServer, handler_class=S, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd... on port {}'.format(port))
    httpd.serve_forever()


def printstuff(var):
    probs = reqcount*100
    return probs

run()

