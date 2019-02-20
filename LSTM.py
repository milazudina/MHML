#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

# https://keras.io/utils/#to_categorical
# labels_categorical = to_categorical(labels_input)
# model_input_acc = model_input[:,:,2:5]

labels_train_cat = to_categorical(labels_train)
labels_test_cat = to_categorical(labels_test)


def evaluate_model(X_train, labels_train_cat, X_test, labels_test_cat):
	verbose, epochs = 1, 100
	n_timesteps, n_features, n_outputs = X_train.shape[1], X_train.shape[2], labels_train_cat.shape[1]
	model = Sequential()
	model.add(LSTM(i, input_shape=(n_timesteps,n_features)))
	model.add(Dropout(0.5))
	model.add(Dense(100, activation='relu'))
	model.add(Dense(n_outputs, activation='sigmoid')) #used to be softmax
	model.compile(Adam(lr=1e-2), loss='categorical_crossentropy', metrics=['accuracy'])
	# fit network
	model.fit(X_train, labels_train_cat, epochs=epochs, batch_size=batch_size, verbose=verbose)
	# evaluate model
	_, accuracy = model.evaluate(X_test, labels_test_cat, batch_size=batch_size, verbose=verbose)
	return accuracy

epochs = [30, 100, 300, 1000]
epochs = np.array(epochs)


scores_over_repeats = list()
repeats = 5
for r in range(0, repeats):
    scores = list()
    for i in epochs:
        	score = evaluate_model(X_train, labels_train_cat, X_test, labels_test_cat)
        	score = score * 100.0
        	print('>#%d: %.3f' % (r+1, score))
        	scores.append(score)
    scores_over_repeats.append(scores)

