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

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(Adam(lr=1e-4), loss='categorical_crossentropy', metrics=['accuracy'])
score = loaded_model.evaluate(X_test, labels_test_cat, verbose=1)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))

def predict_step(n):
    current_step = steps_stack[n,:,:]
    current_step = current_step.reshape(1,30,9)
    prediction = model.predict(current_step)
    return prediction


prediction = predict_step(567)
print(prediction)
true_label = steps_labels[567]
print(true_label)
