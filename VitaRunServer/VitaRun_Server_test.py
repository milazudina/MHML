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
        #print(str(self.headers))

        
        # test for LOGIN
        key = str(self.headers).split()[0] 
        value = str(self.headers).split()[1]

        print("Key:", key)
        print("Value:", value, "\n")

        if (key in "features:"):
            # When Client requests to return features (pronationType, avgFreq and nSteps):
            
            # First check that enough data has been posted to return features
            try:
                # 1. Return the type of the majority of the steps of the last 1500+ samples
                predictionMode = int(stats.mode(wholeRunStepTypes[-1])[0])
                stepsBuffer.clear()
                print("Prediction for this buffer:", predictionMode, "\n")
                print("Frequencies for this buffer:", frequenciesBuffer, "\n")
                # 2. Return average frequency of the last 1500 samples
                # 2.1) return mean frequency in the buffer
                avgFreq = np.mean(frequenciesBuffer)
                # 2.2) empty the buffer
                frequenciesBuffer.clear()
                print("Average frequency for this buffer:", avgFreq, "\n")
                
                # 3. Return the number of steps for this run so far
                flatWholeRunStepTypes = np.concatenate(wholeRunStepTypes).ravel()
                nSteps = flatWholeRunStepTypes.shape[0]
                print("Number of steps in this run so far:", nSteps, "\n")

                # Now send it off
                features = json.dumps({'type': predictionMode, 'freq': avgFreq, 'totalNum': nSteps}, separators=(',',':'))
                print("Returned", str(features), "\n")
                self.wfile.write(features.encode('utf-8'))
             
            # If not enough data
            except IndexError:
                features = json.dumps({'type': 'not enough steps', 'freq': 'not enough steps', 'totalNum': 'not enough steps'}, separators=(',',':'))
                self.wfile.write(features.encode('utf-8'))
                print("Returned Not-Enough-Data warning\n")
 
           
        elif (key in "recommendations:"):
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
            wholeRunFrequencies.clear()
            wholeRunStepTypes.clear()
            
            
        elif (key in "endRun:"):
            username = value
            print(username)
            endTime = datetime.datetime.now()
            endTimeString = endTime.strftime("%Y-%m-%d %H:%M:%S")
            print(endTimeString)
            # Return:
            # number of steps for the whole run
            flatWholeRunStepTypes = np.concatenate(wholeRunStepTypes).ravel()
            nSteps = flatWholeRunStepTypes.shape[0]
            
            # majority type for the whole run and n of steps of each type
            predictionMode = int(stats.mode(flatWholeRunStepTypes)[0])
            counts = np.bincount(flatWholeRunStepTypes)
            
            # frequency for the whole run
            flatWholeRunFrequencies = np.concatenate(wholeRunFrequencies).ravel()
            
            # average frequency
            avgFreq = np.mean(flatWholeRunFrequencies)
            
            # write the run summary into a csv
            writeHistory(username, startTimeHolder[0], endTimeString, nSteps, counts[0], counts[1], counts[2])
            
            # send frequencies for plotting
            endRunJson = json.dumps({'type': predictionMode, 'freq': avgFreq, 'totalNum': nSteps, 'freqWholeRun': flatWholeRunFrequencies}, separators=(',',':'))
            self.wfile.write(endRunJson.encode('utf-8'))
            
            # clears all the data accumulated during the run
            wholeRunFrequencies.clear()
            wholeRunStepTypes.clear()


        elif (key in "historicRuns:"):
            # takes username from login or getUserDetails (in case username has been changed by setUserDetails)
            username = usernameHolder[-1]
            
            # checks for no log in
            if username == 'not logged in':
                self.wfile.write(str(False).encode('utf-8'))
                print("User is not logged in")
            else: 
                userHistoryJson = readHistoryFile(username)
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
            usernameHolder.append(username)
            userDetails = getUserDetails(username)
            userDetailsJson = json.dumps(userDetails)
            print(userDetails)
            self.wfile.write(userDetailsJson.encode('utf-8'))
            

       
    def do_POST(self):
        self._set_response()
        
        # decode  the current batch of samples into format used by functions
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        postDataDict = json.loads(post_data.decode('utf-8'))
        stepsBatch = np.array(list(postDataDict.values()))
        
        
        stepsBuffer.append(stepsBatch)
        currentBatchFreq = local_running_frequency(stepsBatch, 256)
        frequenciesBuffer.append(currentBatchFreq)
        addFreq(usernameHolder[-1], currentBatchFreq)
        print("Frequency of this batch:", currentBatchFreq)
        # add a check that dim = 128 * 9
        flatStepsBuffer = np.vstack(stepsBuffer)
        print("flatStepsBuffer shape:", flatStepsBuffer.shape)
        if flatStepsBuffer.shape[0] > 1500:
            # 1) divide them into steps
            stepsStack = splitter(flatStepsBuffer[:,:9], flatStepsBuffer[:,9])
            print("stepsStack shape:", stepsStack.shape)
            
            # 2) predict the type of each step in steps stack and return the mode
            typePrediction = predictStepType(stepsStack, pronationClassifier, 30)
            typePredictionList = typePrediction.tolist()
            # 3) add to csv file 
            addPronation(usernameHolder[-1], typePredictionList)
            wholeRunStepTypes.append(typePrediction) 

        
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
usernameHolder = ['not logged in']

# this list (when flattened) contains a 0,1 or 2 for each step
# length = n of steps classified
 
run()
