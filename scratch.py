#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:37:17 2019

@author: mila
"""

#steps_filename = '/Users/mila/Bioengineering_Year_4/MHML/pronation_classification/Steps.csv'
#steps = pd.read_csv(steps_filenames, header=0, sep = ',', usecols = [8, 9, 10], dtype = np.float64)
#
#steps = steps.values
#time = np.arange(0, len(steps)/frequency, time_step)
#fig = plt.figure()
#plt.plot(time, steps[:,0])
#plt.plot(time, steps[:,1])
#plt.plot(time, steps[:,2])

n_timesteps, n_features, n_outputs = model_input.shape[1], model_input.shape[2], labels_input.shape[0]

#t = np.arange(len(model_input[1,:,1]))
#
#for j in range(0,len(model_input[:,1,1])):
#    plt.plot(t, model_input[j,:,5])


from keras.utils import to_categorical
labels_categorical = to_categorical(labels_input)

model.fit(model_input, labels_categorical, epochs=epochs, verbose=verbose, validation_split=0.1)
h, accuracy = model.evaluate(model_input, labels_categorical, verbose = verbose)

scores = list()
for r in range(repeats):
	score = evaluate_model(trainX, trainy, testX, testy)
	score = score * 100.0
	print('>#%d: %.3f' % (r+1, score))
	scores.append(score)