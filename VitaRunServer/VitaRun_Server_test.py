#from http.server import SimpleHTTPRequestHandler, HTTPServer
#import logging
#muh_data = []
#class S(SimpleHTTPRequestHandler):
#
#    def _set_response(self):
#        self.send_response(200)
#        self.send_header('Conent-type', 'text/html')
#        self.end_headers()
#
#    def do_GET(self):
#        print(str(self.headers))
#        self._set_response()
#        self.wfile.write("GET request received".encode('utf-8'))
#
#    def do_POST(self):
#        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
#        post_data = self.rfile.read(content_length) # <--- Gets the data itself
#        print(post_data.decode('utf-8'))
#        processstring(data)
#        muh_data.append(post_data.decode('utf-8'))
#        self._set_response()
#        self.wfile.write("POST request received".encode('utf-8'))
#
#def run(server_class = HTTPServer, handler_class=S, port=3000):
#    server_address = ('146.169.177.229', port)
#    httpd = server_class(server_address, handler_class)
#    print('Starting httpd... on port {}'.format(port))
#    httpd.serve_forever()
#
#def process_string(data) {
#        is (string a username) {
#                do username stuff
#        }
#        is string data:
#            do ML on data
#            return ML'd data.'
#   }
#
#run()

from http.server import SimpleHTTPRequestHandler, HTTPServer
from mlFunctions import loadPronationClassifier
from mlFunctions import predictStepType

import logging
import json
import numpy as np

class S(SimpleHTTPRequestHandler):
    

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print(str(self.headers).split()[1])
        self._set_response()
        keyword = str(self.headers).split()[1] 
        print(str(self.headers))
        self.wfile.write("GET request received".encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        postDataDict = json.loads(post_data.decode('utf-8'))
        stepsBatch = np.array(list(postDataDict.values()))
        # here we should have functions from N
        print(stepsBatch.shape)
        predictions = predictStepType(stepsBatch, pronationClassifier)
        print(predictions)
        self._set_response()
        self.wfile.write("POST request received".encode('utf-8'))
        

# this function starts the server and loads the ML model
def run(server_class = HTTPServer, handler_class=S, port=3000, model_name = 'model'):
    server_address = ('', port)
    # create a server
    httpd = server_class(server_address, handler_class)
    #pronationClassifier = loadPronationClassifier()
    print('Starting httpd... on port {}'.format(port))
    #print(pronationClassifier.summary())
    httpd.serve_forever() 
    
pronationClassifier = loadPronationClassifier()
    
#def f(stepsBatch):
#    predictStepType(stepsBatch, pronationClassifier)

   
#inputFile= list(post_data.values())
#
#    # inputFile =  json.dumps(post_data.values())#open json file
#    with open('./' + username + '/'+ filename, 'a') as outputFile:#load csv file
#        writer = csv.writer(outputFile)
#        writer.writerow(inputFile)

run()
