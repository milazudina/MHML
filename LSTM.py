#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Flatten
from keras.utils import to_categorical
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split, StratifiedKFold
import h5py

# https://machinelearningmastery.com/how-to-develop-rnn-models-for-human-activity-recognition-time-series-classification/

# The output for the model will be a vector containing the probability
# of a given step belonging to each of the pronation classes

# https://keras.io/

# https://keras.io/utils/#to_categorical
# labels_categorical = to_categorical(labels_input)
# model_input_acc = model_input[:,:,2:5]

#labels_train_cat = to_categorical(labels_train)
#labels_test_cat = to_categorical(labels_test)

#k = 5
#folds = list(StratifiedKFold(n_splits=k, shuffle=True, random_state=1).split(X_train, labels_train_cat))

from sklearn.utils import class_weight


def evaluate_model(X_train, labels_train_cat, X_test, labels_test_cat):
    verbose, epochs, batch_size = 1, 10, 64
    n_timesteps, n_features, n_outputs = X_train.shape[1], X_train.shape[2], labels_train_cat.shape[1]
    # create model
    model = Sequential()
    model.add(LSTM(100, return_sequences=True, input_shape=(n_timesteps,n_features)))
    model.add(LSTM(100, return_sequences=True))
    model.add(LSTM(100))
    model.add(Dropout(0.5))
    model.add(Dense(100, activation='relu'))
    
    model.add(Dense(n_outputs, activation='softmax')) #used to be softmax
    # compile model
    model.compile(Adam(lr=1e-4), loss='categorical_crossentropy', metrics=['accuracy'])
    # fit network
    model.fit(X_train, labels_train_cat, epochs=epochs, 
           batch_size=batch_size, 
           verbose=verbose, 
           class_weight=class_weights,
           validation_split = 0.2)
    # evaluate model
    predictions = model.predict(X_test)
    _, accuracy = model.evaluate(X_test, labels_test_cat, batch_size=batch_size, verbose=verbose)
    #summary = model.summary()
    #model.save('/Users/mila/Bioengineering_Year_4/MHML/pronation_classification/model.h5')
    return accuracy, predictions, model




#epochs = [40, 100, 400, 1000]
#epochs = np.array(epochs)




scores_over_repeats = list()
repeats = 5
for p in range(9,14):
    train_indices = np.argwhere(np.array(person_labels) != p)
    test_indices = np.argwhere(np.array(person_labels) == p)
    X_train = steps_stack[train_indices[:,0], :, :]
    X_test = steps_stack[test_indices[:,0], :, :]
    steps_labels = np.array(steps_labels)
    y_train = steps_labels[train_indices[:,0]]
    y_test = steps_labels[test_indices[:,0]]
        
    # X_train = steps_stack indices not equal to p
    # X_test = indices of p    
    # X_train, X_test, labels_train, labels_test = train_test_split(steps_stack, steps_labels, test_size = 0.2)
    labels_train_cat = to_categorical(y_train)
    labels_test_cat = to_categorical(y_test)
    class_weights = class_weight.compute_class_weight('balanced',
                                                 np.unique(labels_train),
                                                 labels_train)
#    scores = list()
#    for i in epochs:
    score, predictions, model = evaluate_model(X_train, labels_train_cat, X_test, labels_test_cat)
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("model.h5")
    print("Saved model to disk")
    #print(summary)
    #print(predictions)
    score = score * 100.0
    print('>#%d: %.3f' % (r+1, score))
#            scores.append(score)
#    scores_over_repeats.append(scores)

