#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:31:34 2019

@author: mila
"""
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Flatten
from keras.utils import to_categorical
from keras.optimizers import Adam

# https://machinelearningmastery.com/how-to-develop-rnn-models-for-human-activity-recognition-time-series-classification/

# The output for the model will be a vector containing the probability
# of a given step belonging to each of the pronation classes

# https://keras.io/

#https://keras.io/utils/#to_categorical
labels_categorical = to_categorical(labels_input)

model_input_acc = copy.model_input

def evaluate_model(model_input_acc, labels_categorical):
	verbose, epochs, batch_size = 1, 20, 64
	n_timesteps, n_features, n_outputs = model_input.shape[1], model_input.shape[2], labels_categorical.shape[1]
	model = Sequential()
	model.add(LSTM(100, input_shape=(n_timesteps,n_features)))
	model.add(Dropout(0.5))
	model.add(Dense(100, activation='relu'))
	model.add(Dense(n_outputs, activation='sigmoid')) #used to be softmax
	model.compile(Adam(lr=1e-2), loss='categorical_crossentropy', metrics=['accuracy'])
	# fit network
	model.fit(model_input, labels_categorical, epochs=epochs, batch_size=batch_size, verbose=verbose)
	# evaluate model
	_, accuracy = model.evaluate(model_input_acc, labels_categorical, batch_size=batch_size, verbose=1)
	return accuracy



scores = list()
repeats = 1
for r in range(repeats):
	score = evaluate_model(model_input, labels_categorical)
	score = score * 100.0
	print('>#%d: %.3f' % (r+1, score))
	scores.append(score)

for layer in model.layers:
    weights = layer.get_weights()
