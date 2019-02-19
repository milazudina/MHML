#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 12:25:02 2019

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
labels_norbs = to_categorical(steps_labels)

def evaluate_model(steps_stack, norbs):
	verbose, epochs, batch_size = 1, 20, 64
	n_timesteps, n_features, n_outputs = steps_stack.shape[1], steps_stack.shape[2], labels_norbs.shape[1]
	model = Sequential()
	model.add(LSTM(100, input_shape=(n_timesteps,n_features)))
	model.add(Dropout(0.5))
	model.add(Dense(100, activation='relu'))
	model.add(Dense(n_outputs, activation='sigmoid')) #used to be softmax
	model.compile(Adam(lr=1e-2), loss='categorical_crossentropy', metrics=['accuracy'])
	# fit network
	model.fit(steps_stack, labels_norbs, epochs=epochs, batch_size=batch_size, verbose=verbose, validation_split = 0.1)
	# evaluate model
	_, accuracy = model.evaluate(steps_stack, labels_norbs, batch_size=batch_size, verbose=1)
	return accuracy

print(model.summary())

scores = list()
repeats = 1
for r in range(repeats):
	score = evaluate_model(steps_stack, labels_norbs)
	score = score * 100.0
	print('>#%d: %.3f' % (r+1, score))
	scores.append(score)
