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
from userFunctions import login

import logging
import json
import numpy as np


class S(SimpleHTTPRequestHandler):
    
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print(str(self.headers))
        print(type(self.headers))
        
        key = str(self.headers).split()[0] 
        value = str(self.headers).split()[1]

        print("Key:", key)
        print("Value", value)
        print(type(key))
        print(type(value))
        
        self._set_response()
        # 17 is a temporary solution for using with Rested app
        
        if (key in "feature"):
            mostRecentPred = allPredictions[-1]
            self.wfile.write(str(mostRecentPred).encode('utf-8'))
            
            
#        elif (key in "getTypeEOR"):
#            
#            
#            
#        elif (key in "getFreq"):
#            self.wfile.write("GET request received".encode('utf-8'))
#            
#        elif (key in "getTypesEOR"):
#            self.wfile.write()
#            
#        elif (key in "setUser"):
#            self.wfile.write()
#        elif (key in "createProfile"):
            
        elif (key in "getUserDetails:"):
            
        elif (key in "setUserDetails:"):
            
            
        
        elif (key in "login:"):
            print(self.headers)
#            content_length = int(self.headers['Content-Length'])
#            post_data = self.rfile.read(content_length)
            
            json_output = json.loads(value)
            print(json_output)
            print(type(json_output))
            username = json_output["username"]
            password = json_output["password"]
            print('hello')
            print(type(username))
            print(type(password))
            test = login(username, password)
            print(test)

# postPressureData        
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        postDataDict = json.loads(post_data.decode('utf-8'))
        stepsBatch = np.array(list(postDataDict.values()))
        # here we should have functions from N
        print(stepsBatch.shape)
        typePrediction = predictStepType(stepsBatch, pronationClassifier) # probabilities for each step in the batch
        allPredictions.append(typePrediction) # appending to this array to return it at the end of run
        print(allPredictions)
        # need to flatten the list
        print(type(allPredictions))
        self._set_response()
        self.wfile.write("POST request received".encode('utf-8'))
        

# this function starts the server and loads the ML model
def run(server_class = HTTPServer, handler_class=S, port=3000, model_name = 'model'):
    server_address = ('', port)
    # create a server
    httpd = server_class(server_address, handler_class)
    print('Starting httpd... on port {}'.format(port))
    #print(pronationClassifier.summary())
    httpd.serve_forever() 

# this loads the Keras model to classify 
pronationClassifier = loadPronationClassifier()

# this list (when flattened) contains a 0,1 or 2 for each step
# length = n of steps classified
allPredictions = []


allFrequencies = []
 
run()
