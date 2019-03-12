from http.server import SimpleHTTPRequestHandler, HTTPServer
from mlFunctions import loadPronationClassifier, predictStepType
from userFunctions import login, createFiles, setUserDetails, getUserDetails, writeHistory, readHistoryFile, addFreq, addPronation, startRun
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

    def do_GET(self):
        self._set_response()
        print(str(self.headers))

        
        # test for LOGIN
        key = str(self.headers).split()[0] 
        value = str(self.headers).split()[1]
        
        # test for CREATE PROFILE
#        key = str(self.headers).split()[2] 
#        value = str(self.headers).split()[3]
        
        # test for FEATURE EOR
#       endRun: Obie1
#        key = str(self.headers).split()[4] 
#        value = str(self.headers).split()[5]
#       startRun: Obie1
#        key = str(self.headers).split()[16] 
#        value = str(self.headers).split()[17]

        print("Key:", key)
        print("Value:", value)

        if (key in "features:"):
            # When Client requests return features (pronationType, avgFreq and nSteps):
            
            # 1. Return the type of the majority of the steps of the last 1500 samples
            predictionMode = int(stats.mode(wholeRunStepTypes[-1])[0])
            print("prediction for this buffer:", predictionMode)
            

            # 2. Return average frequency of the last 1500 samples
            
            # 2.2) return mean frequency in the buffer
            avgFreq = np.mean(frequenciesBuffer)
            
            # 2.3) empty the buffer
            frequenciesBuffer.clear()
            
            
            # 3. Return the number of steps for this run so far
            flatWholeRunStepTypes = np.concatenate(wholeRunStepTypes).ravel()
            nSteps = flatWholeRunStepTypes.shape[0]

            print(wholeRunStepTypes)
            print(frequenciesBuffer)
        
            allSteps = np.concatenate(wholeRunStepTypes).ravel()
            print(type(allSteps))
            
            
            features = json.dumps({'type': predictionMode, 'freq': avgFreq, 'totalNum': nSteps}, separators=(',',':'))
            self.wfile.write(features.encode('utf-8'))
 
           
        elif (key in "featuresEOR:"):
            # this one will be Kenza's end of run
            flatStepsBuffer = np.vstack(stepsBuffer)
            stepsStack = splitter(flatStepsBuffer)
            # stepsStack should be fed into ML
            allSteps = np.concatenate(allPredictions).ravel()
            print(allSteps)
            featuresEOR = json.dumps({'type': mostRecentPredAvg, 'freq': mostRecentFreqAvg, 'totalNum': nSteps}, separators=(',',':'))
            self.wfile.write(str(allSteps).encode('utf-8'))


        elif (key in "startRun:"):
            username = value
            startTime = datetime.datetime.now()
            startTimeString = startTime.strftime("%Y-%m-%d %H:%M:%S")
            startTimeHolder.append(startTimeString)
            startRun(username)
            
            
        elif (key in "endRun:"):
            username = value
            print(username)
            endTime = datetime.datetime.now()
            endTimeString = endTime.strftime("%Y-%m-%d %H:%M:%S")
            print(endTimeString)
            nSteps = 10
            # write the summary into csv
            writeHistory(username, startTimeHolder[0], endTimeString, 
                         nSteps, 1, 2, 3)
#           # send data for visualisation
#            self.wfile.write(str(frequencies).encode('utf-8'))


        elif (key in "historicRuns:"): #    doesn't work yet
            json_output = json.loads(value)
            # or just using a string in value again
            username = json_output["username"]
            userHistory, nRows = readHistoryFile(username)
            userHistoryJson = json.dumps(userHistory, separators=(',',':'))
            self.wfile.write(userHistoryJson.encode('utf-8'))

            
        elif (key in "login:"):
            json_output = json.loads(value)
#            print(json_output) {'password': '789ab', 'username': 'Mila123'}
#            print(type(json_output)) <class 'dict'>
            username = json_output["username"]
            usernameHolder.append(username)
            password = json_output["password"]
#            print(type(username)) <class 'str'>
#            print(type(password)) <class 'str'>
            loginReturn = login(username, password)
            print(loginReturn)
            self.wfile.write(str(loginReturn).encode('utf-8'))

        
        elif (key in "createProfile:"):
            json_output = json.loads(value)
            name = json_output["name"]
            username = json_output["username"]
            password = json_output["password"]
            age = json_output["age"]
            weight = json_output["weight"]
            createFilesReturn = createFiles(username, password, name, age, weight)
            print(createFilesReturn)
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
            username = value
            userDetails = getUserDetails(username)
            userDetailsJson = json.dumps(userDetails)
            print(userDetails)
            self.wfile.write(userDetailsJson.encode('utf-8'))
            

       
    def do_POST(self):
        usernameHolder = 'Norb456'
        self._set_response()
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        postDataDict = json.loads(post_data.decode('utf-8'))
#        print(postDataDict)
        stepsBatch = np.array(list(postDataDict.values()))
        stepsBuffer.append(stepsBatch)
        currentBatchFreq = local_running_frequency(stepsBatch, 256)
        frequenciesBuffer.append(currentBatchFreq)
#        print(frequenciesBuffer)
        addFreq(usernameHolder, currentBatchFreq)
        print("Frequency of current 128 samples:", currentBatchFreq)
        print(stepsBuffer)
        # add a check that dim = 128 * 9
        flatStepsBuffer = np.vstack(stepsBuffer)
        print("flatStepsBuffer shape:", flatStepsBuffer.shape)
        if flatStepsBuffer.shape[0] > 1500:
            # 1.2) divide them into steps
            stepsStack = splitter(flatStepsBuffer[:,:9], flatStepsBuffer[:,9])
            print("stepsStack shape:", stepsStack.shape)
            
            # 1.3) predict the type of each step in steps stack and return the mode
            typePrediction = predictStepType(stepsStack, pronationClassifier, 30)
            print("array of predictions:", typePrediction)
            addPronation(usernameHolder[0], typePrediction)

            wholeRunStepTypes.append(typePrediction) 
            
            # 1.4) buffer is emptied
            stepsBuffer.clear()


        
        
        
        # that needs to be cleared every time we call pronation classifier
        # that needs to be done differently

        # here we should have functions from N
#        print(asstepsBuffer.shape)

        #print(type(allPredictions)) list
        
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

frequenciesBuffer = []
wholeRunFrequencies = []
wholeRunStepTypes = []
stepsBuffer = []
startTimeHolder = []
usernameHolder = []

# this list (when flattened) contains a 0,1 or 2 for each step
# length = n of steps classified
 
run()
