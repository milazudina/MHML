import pandas
import matplotlib as plt
import numpy as np
#
from scipy.spatial.distance import pdist, squareform #scipy spatial distance
import sklearn as sk
import sklearn.metrics.pairwise


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

# 

steps = pd.read_csv('/Users/mila/Bioengineering_Year_4/MHML/pronation_classification/data/v3/teststeps2.csv', 
                    header = None,
                    sep = ',',
                    usecols = [0, 2, 3, 4, 5, 6, 8, 9, 10])
steps = steps.values

labels_for_steps = pd.read_csv('/Users/mila/Bioengineering_Year_4/MHML/pronation_classification/data/v3/testlabel2.csv',
                               header = None, sep = ',')
norbs_labels = labels_for_steps.values

#steps_with_labels_norbs = np.concatenate((steps, norbs_labels), axis=1)
steps_with_labels_norbs = np.hstack((steps, norbs_labels))

all_types = []
for j in range(1,4):
    types = []
    for i in range(0, len(steps_with_labels_norbs)):
#        col number below is where the pronation label is found
        if steps_with_labels_norbs[i, len(steps_with_labels_norbs[1,:])-1] == j:
            types.append(steps_with_labels_norbs[i,:])
    types = np.array(types)
    all_types.append(types)

steps = []
steps_labels = []
person_labels = []
count = 0
for j in range(0,3):
#    the magical number below is the length of the step - 30 rn
    for i in range(0, len(all_types[j]), 30): 
#   the number of :col is the sensor data
        step = np.array(all_types[j][i:i+30, :len(steps_with_labels_norbs[1,:])-3])
        steps.append(step)
        steps_labels.append(norbs_labels[count, 2]-1)
        person_labels.append(norbs_labels[count, 1])
        count = count + 30
        

#del steps[-1]
#del steps_labels[-1]
#del steps[263]
#del steps_labels[263]
steps_stack = np.stack(steps, axis = 0) 

#t = np.arange(0,30)/50
#for j in range(0,len(steps_stack[:,1,0])):     
#    plt.plot(t, steps_stack[j,:,0])

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
   
    
    
