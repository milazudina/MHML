from http.server import SimpleHTTPRequestHandler, HTTPServer
# from mlFunctions import loadPronationClassifier, predictStepType
# from userFunctions import login, createFiles, setUserDetails, getUserDetails, writeHistory, readHistoryFile, addFreq, addPronation, startRun
from processFunctions import local_running_frequency, splitter, running_frequency

import json
import numpy as np
import scipy.stats as stats
import datetime


class S(SimpleHTTPRequestHandler):
    
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

       
    def do_POST(self):
        usernameHolder = 'Norb456'
        self._set_response()
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print(post_data.decode('utf-8'))

        postDataDict = json.loads(post_data.decode('utf-8'))
#        print(postDataDict)
        stepsBatch = np.array(list(postDataDict.values()))
        stepsBuffer.append(stepsBatch)
        currentBatchFreq = local_running_frequency(stepsBatch[:,:9], 256)
        print(currentBatchFreq*2*60)
        print(type(currentBatchFreq))
        frequenciesBuffer.append(currentBatchFreq)
#        print(frequenciesBuffer)
#         addFreq(usernameHolder, currentBatchFreq)
        print("Frequency of current 256 samples:", currentBatchFreq)
        print(stepsBuffer)
        # add a check that dim = 128 * 9
        flatStepsBuffer = np.vstack(stepsBuffer)
        print("flatStepsBuffer shape:", flatStepsBuffer.shape)
        if flatStepsBuffer.shape[0] > 1500:
            # 1.2) divide them into steps
            stepsStack = splitter(flatStepsBuffer[:,:9], flatStepsBuffer[:,9], True)
            print("stepsStack shape:", stepsStack.shape)
#
#             # 1.3) predict the type of each step in steps stack and return the mode
#             typePrediction = predictStepType(stepsStack, pronationClassifier, 30)
#             print("array of predictions:", typePrediction)
#             addPronation(usernameHolder[0], typePrediction)
#
#             wholeRunStepTypes.append(typePrediction)
#
#             # 1.4) buffer is emptied
#             stepsBuffer.clear()
#
#
#
#
#
#         # that needs to be cleared every time we call pronation classifier
#         # that needs to be done differently
#
#         # here we should have functions from N
# #        print(asstepsBuffer.shape)
#
#         #print(type(allPredictions)) list
#
#         self.wfile.write("POST request received".encode('utf-8'))
        

# this function starts the server and loads the ML model
def run(server_class = HTTPServer, handler_class=S, port=3000, model_name = 'model'):
    server_address = ('', port)
    # create a server
    httpd = server_class(server_address, handler_class)
    print('Starting httpd... on port {}'.format(port))
    #print(pronationClassifier.summary())
    httpd.serve_forever() 

# this loads the Keras model to classify 
# pronationClassifier = loadPronationClassifier()

frequenciesBuffer = []
wholeRunFrequencies = []
wholeRunStepTypes = []
stepsBuffer = []
startTimeHolder = []
usernameHolder = []

# this list (when flattened) contains a 0,1 or 2 for each step
# length = n of steps classified
 
run()
