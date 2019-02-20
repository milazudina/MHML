 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

# cnn lstm model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import TimeDistributed
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.utils import to_categorical
from matplotlib import pyplot

labels_categorical = to_categorical(labels_input)
model_input_acc = model_input[:,:,2:5]
n_timesteps, n_features, n_outputs = model_input.shape[1], model_input.shape[2], labels_categorical.shape[1]
n_steps, n_length = 4, 9
verbose, epochs, batch_size = 1, 25, 64
cnn_lstm_input = model_input.reshape((model_input.shape[0], n_steps, n_length, n_features))

# define model
model = Sequential()
model.add(TimeDistributed(Conv1D(filters=64, kernel_size=3, activation='relu'), input_shape=(None, n_length, n_features)))
model.add(TimeDistributed(Conv1D(filters=64, kernel_size=3, activation='relu')))
model.add(TimeDistributed(Dropout(0.5)))
model.add(TimeDistributed(MaxPooling1D(pool_size=2)))
model.add(TimeDistributed(Flatten()))
model.add(LSTM(100))
model.add(Dropout(0.5))
model.add(Dense(100, activation='relu'))
model.add(Dense(n_outputs, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit network
model.fit(cnn_lstm_input, labels_categorical, epochs=epochs, batch_size=batch_size, verbose=verbose)
# evaluate model
_, accuracy = model.evaluate(cnn_lstm_input, labels_categorical, batch_size=batch_size, verbose=1)
