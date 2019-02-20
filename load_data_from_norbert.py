import pandas
import matplotlib as plt
import numpy as np
from scipy.spatial.distance import pdist, squareform #scipy spatial distance
import sklearn as sk
import sklearn.metrics.pairwise
import matplotlib.pyplot as plt

# Load data

# load a single file as a numpy array
#def load_file(filepath):
#	dataframe = read_csv(filepath, header=None, delim_whitespace=True)
#	return dataframe.values


# 1 - normal
# 2 - over
# 3 - under
#
#def recurrence_plot(s, eps=None, steps=None):
#    if eps==None: eps=0.1
#    if steps==None: steps=10
#    d = sk.metrics.pairwise.pairwise_distances(s)
#    d = np.floor(d / eps)
#    d[d > steps] = steps
#    #Z = squareform(d)
#    return d 
#   
#fig = plt.figure(figsize=(15,14))
#random_series = np.random.random(1000)
#ax = fig.add_subplot(1, 2, 1)
#ax.imshow(recurrence_plot(random_series[:,None]))
#sinus_series = np.sin(np.linspace(0,24,1000))
#ax = fig.add_subplot(1, 2, 2)
#ax.imshow(recurrence_plot(sinus_series[:,None]));
#

import pandas as pd

steps = pd.read_csv('/Users/mila/Bioengineering_Year_4/MHML/pronation_classification/Steps.csv', 
                    header = None,
                    sep = ',', 
                    usecols = [8, 9, 10])
steps = steps.values

labels_for_steps = pd.read_csv('/Users/mila/Bioengineering_Year_4/MHML/pronation_classification/Labels.csv',
                               header = None, sep = ',')
norbs_labels = labels_for_steps.values

#steps_with_labels_norbs = np.concatenate((steps, norbs_labels), axis=1)
steps_with_labels_norbs = np.hstack((steps, norbs_labels))

all_types = []
for j in range(1,4):
    types = []
    for i in range(0, len(steps_with_labels_norbs)):
        if steps_with_labels_norbs[i,4] == j:
            types.append(steps_with_labels_norbs[i,:])
    types = np.array(types)
    all_types.append(types)

steps = []
steps_labels = []
for j in range(0,3):
    for i in range(0, len(all_types[j]), 38):
        step = np.array(all_types[j][i:i+38, :3])
        steps.append(step)
        steps_labels.append(j)

del steps[-1]
del steps_labels[-1]
del steps[263]
del steps_labels[263]
steps_stack = np.stack(steps, axis = 0) 

t = np.arange(0,38)/50
for j in range(0,len(steps_stack[:,1,1])):     
    plt.plot(t, steps_stack[j,:,1])

##equal_steps_norbs = []
#labels_norbs = []  
#splitting_norbs = []
#for j in range(0,3):
#    print(np.bincount(all_types[j][:,3]))
#    #n_steps = len(np.bincount(all_types[j][:,3]))
#    for i in range(0, len(all_types[j])-1):
#        all_types[j][i+1,4] = all_types[j][i+1, 3] - all_types[j][i, 3]
#    for i in range(0, len(all_types[j])):  
#        if all_types[j][i, 4] == 1:
#            splitting_norbs.append(i)
#            labels_norbs.append(j)
#            
#splitting_norbs = np.array(splitting_norbs)
#all_steps = []
#for j in range(0,3):
#    for y in range(0, len(all_types[j])):
#        all_steps.append(all_types[j][y,:3])
#all_steps = np.array(all_steps)
#equal_steps_norbs = np.split(all_steps, splitting_indices)
# 
#t = np.arange(0,len(all_steps))  

    
#    for i in range(0, n_steps):
#        step = []
#        for k in range(0, 38):
#            substep = []
#            if all_types[j][k, 4] == i+1:
#                substep.append(all_types[j][k, :3])
#            step = np.array(substep)
#            equal_steps_norbs.append(step)
#        labels_norbs.append(all_types[j][i,4])
   
    
    
