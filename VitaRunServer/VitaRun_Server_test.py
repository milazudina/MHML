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
from mlFunctions import loadPronationClassifier, predictStepType
from userFunctions import login, createFiles, setUserDetails, getUserDetails
from processFunctions import running_frequency, splitter

import json
import numpy as np
import scipy.stats as stats


class S(SimpleHTTPRequestHandler):
    
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print(str(self.headers))
        
#        key = str(self.headers).split()[0] 
#        value = str(self.headers).split()[1]


        
        self._set_response()
        
        # test for LOGIN
#        key = str(self.headers).split()[16] 
#        value = str(self.headers).split()[17]
        
        # test for CREATE PROFILE
        key = str(self.headers).split()[2] 
        value = str(self.headers).split()[3]
        
        # test for FEATURE EOR
#        key = str(self.headers).split()[13] 
#        value = str(self.headers).split()[14]

        print("Key:", key) # <class 'str'>
        print("Value:", value) # <class 'str'>


        if (key in "features:"):
            mostRecentPredAvg = int(stats.mode(allPredictions[-1])[0])
            mostRecentFreqAvg = 180
            allSteps = np.concatenate(allPredictions).ravel()
            print(type(allSteps))
            nSteps = allSteps.shape[0]
#            mostRecentAvgFreq = allFrequencies[-1] an average of this
            features = json.dumps({'type': mostRecentPredAvg, 'freq': mostRecentFreqAvg, 'totalNum': nSteps}, separators=(',',':'))
            self.wfile.write(features.encode('utf-8'))
 
           
        elif (key in "featuresEOR:"):
            flatStepsBuffer = np.concatenate(stepsBuffer).ravel()
            stepsStack = splitter(flatStepsBuffer)
            # stepsStack should be fed into ML
            allSteps = np.concatenate(allPredictions).ravel()
            print(allSteps)
            featuresEOR = json.dumps({'type': mostRecentPredAvg, 'freq': mostRecentFreqAvg, 'totalNum': nSteps}, separators=(',',':'))
            self.wfile.write(str(allSteps).encode('utf-8'))


#        elif (key in "startRun:"):
#            record the time
            
#        elif (key in "finishRun:"):
#            write all the data into csv
#            send data for visualisation
#            self.wfile.write(str(loginReturn).encode('utf-8'))

#        elif (key in "historicRuns:"):
#            return a json with a csv file historic run
#            self.wfile.write(str(loginReturn).encode('utf-8'))
            
        elif (key in "login:"):
            json_output = json.loads(value)
#            print(json_output) {'password': '789ab', 'username': 'Mila123'}
#            print(type(json_output)) <class 'dict'>
            username = json_output["username"]
            password = json_output["password"]
#            print(type(username)) <class 'str'>
#            print(type(password)) <class 'str'>
            loginReturn = login(username, password)
            self.wfile.write(str(loginReturn).encode('utf-8'))
        
        elif (key in "createProfile:"):
            json_output = json.loads(value)
            name = json_output["name"]
            username = json_output["username"]
            password = json_output["password"]
            age = json_output["age"]
            weight = json_output["weight"]
            createFilesReturn = createFiles(username, password, name, age, weight)
            self.wfile.write(str(createFilesReturn).encode('utf-8'))
            
        elif (key in "setUserDetails:"):
            json_output = json.loads(value)
            name = json_output["name"]
            username = json_output["username"]
            password = json_output["password"]
            age = json_output["age"]
            weight = json_output["weight"]
            setUserDetails(username, password, name, age, weight)
            
        elif (key in "getUserDetails:"):
            json_output = json.loads(value)
            name = json_output["name"]
            username = json_output["username"]
            password = json_output["password"]
            age = json_output["age"]
            weight = json_output["weight"]
            getUserDetails(username, password, name, age, weight)
            
# postPressureData        
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        postDataDict = json.loads(post_data.decode('utf-8'))
        stepsBatch = np.array(list(postDataDict.values()))
        
        # add a check that dim = 128 * 9
        currentBatchFreq = running_frequency(stepsBatch)
        allFrequencies.append(currentBatchFreq)
        stepsBuffer.append(stepsBatch)
        # that needs to be cleared every time we call pronation classifier
        flatStepsBuffer = np.concatenate(stepsBuffer).ravel()
        print(flatStepsBuffer) 
        # here we should have functions from N
#        print(asstepsBuffer.shape)
        typePrediction = predictStepType(stepsBatch, pronationClassifier, 30) # probabilities for each step in the batch
        allPredictions.append(typePrediction) # appending to this array to return it at the end of run
        print(allPredictions)
        print(allFrequencies)
        #print(type(allPredictions)) list
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
stepsBuffer = []
 
run()
