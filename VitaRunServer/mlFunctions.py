#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:51:07 2019

@author: mila
"""

#nodes_before_500 = np.arange(10,500,20)
#nodes_after_500 = np.arange(500,1000,50)
#nodes = np.concatenate((nodes_before_500, nodes_after_500), axis = 0)
#print(nodes)

#train_indices = np.argwhere(np.array(person_labels) != p)
#test_indices = np.argwhere(np.array(person_labels) == p)
#X_train = steps_stack[train_indices[:,0], :, :]
#X_test = steps_stack[test_indices[:,0], :, :]
#
#
#steps_labels = np.array(steps_labels)
#y_train = steps_labels[train_indices[:,0]]
#y_test = steps_labels[test_indices[:,0]]

# load json and create model
from keras.models import model_from_json
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Flatten
from keras.utils import to_categorical
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split, StratifiedKFold
import h5py
import numpy as np


def loadPronationClassifier(model_name = 'model'):
    json_file = open(str(model_name) + '.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(str(model_name) + '.h5')
    print('Loaded model from disk')
    return loaded_model

 # returns type of each step into an array
 # array then concatenated
def predictStepType(stepsBatch, loaded_model, stepLength): # numpy array of 30, 9
    nSteps = int(stepsBatch.shape[0]/stepLength)
    current_step = stepsBatch.reshape(nSteps, 30, 9)
    probabilities = loaded_model.predict(current_step)
    predictions = probabilities[:,:]
    
    typePrediction = np.zeros((probabilities.shape[0]))
    for i in range(0, probabilities.shape[0]):
        predictions[i,:] = probabilities[i, :] == np.max(probabilities[i, :])
        typePrediction[i] = int(np.argmax(predictions[i, :]))
    typePrediction = typePrediction.astype(int)
    return typePrediction # returns predictions for all steps in the batch

def getPredictionMode(predictions):
    
    return stepType

def getTypesEOR():
    return countNP, countOP, countUP


## evaluate loaded model on test data
#loaded_model.compile(Adam(lr=1e-4), loss='categorical_crossentropy', metrics=['accuracy'])
#score = loaded_model.evaluate(X_test, labels_test_cat, verbose=1)
#print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
#
## instead of n, make the input 
#
#def predict_step(n):
#    current_step = steps_stack[n,:,:]
#    current_step = current_step.reshape(1,30,9)
#    prediction = model.predict(current_step)
#    return prediction
#
#
#prediction = predict_step(100)
#print(prediction)
#true_label = steps_labels[100]
#print(true_label)
