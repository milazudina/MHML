#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import pkg_resources
import math
import os
import scipy.signal as signal

#print(pkg_resources.get_distribution("pandas").version)

################### Define important things ######################################
normal_filenames = '/Users/mila/Bioengineering_Year_4/MHML/pronation_classification/runs/{}_normal_50hz.csv'
inversion_filenames = '/Users/mila/Bioengineering_Year_4/MHML/pronation_classification/runs/{}_inversion_50hz.csv'
eversion_filenames = '/Users/mila/Bioengineering_Year_4/MHML/pronation_classification/runs/{}_eversion_50hz.csv'
pronation_type_filenames = [str(normal_filenames), str(inversion_filenames), str(eversion_filenames)]
num_of_participants = 6
fs = 50 # sampling frequency

################### DEFINE THE FUNCTIONS ########################################

def load_runs(filename):
    runs = []
    #for filename in os.listdir(path):
    for i in ([1,2,3,5,6]):
        runs.append(pd.read_csv(filename.format(i), header=0, sep = ',', usecols = [3, 6, 11, 12, 13], dtype = np.float64))
    concatenated_runs = pd.concat(runs)
    return(concatenated_runs.values)


def add_acc_magnitude(sensors_series, ax=2, ay=3, az=4):
    sensors_series_with_acc_mag = np.zeros((len(sensors_series), len(sensors_series[1,:])+1))
    sensors_series_with_acc_mag[:,:-1] = sensors_series
    for i in range (0, len(sensors_series)):
        sensors_series_with_acc_mag[i, len(sensors_series_with_acc_mag[1,:])-1] = math.sqrt(sensors_series_with_acc_mag[i, 2]**2 + 
                                 sensors_series_with_acc_mag[i, 3]**2 + sensors_series_with_acc_mag[i, 4]**2)
    return(sensors_series_with_acc_mag)



def get_gradient(series):
    gradient = np.zeros((len(series)))
    for i in range (0, len(series)-1):
        gradient[i] = series[i+1] - series[i]
    return(gradient)


        
def add_gradient(sensor_series_with_magnitude, which_col = 5, my_grad = True, np_grad = False):
    sensor_series_with_gradient = np.zeros((len(sensor_series_with_magnitude), len(sensor_series_with_magnitude[1,:])+1))
    sensor_series_with_gradient[:,:-1] = sensor_series_with_magnitude
    #gradient = np.zeros( (len(sensor_series_with_magnitude[:,1]) ) )
    if my_grad == True:
        for i in range (0, len(sensor_series_with_gradient)-1):
            print('j')
            sensor_series_with_gradient[i, len(sensor_series_with_gradient[1,:])-1] = sensor_series_with_gradient[i+1, which_col] - sensor_series_with_gradient[i, which_col]
    if np_grad == True:
        sensor_series_with_gradient[i, len(sensor_series_with_gradient[1,:])-1] = np.gradient[:, which_col]
    return(sensor_series_with_gradient)



# 1) normal 2) inversion 3) eversion  
def load_and_add_features(pronation_type_filenames, my_grad = True, np_grad = False, which_col = 5):
    sensor_series_with_feat = []
    for index, filename in enumerate(pronation_type_filenames):
        sensor_series = load_runs(filename)
        sensor_series_with_magnitude = add_acc_magnitude(sensor_series)
        #sensor_series_with_gradient = add_gradient(sensor_series_with_magnitude, which_col, np_grad)
        sensor_series_with_feat.append(sensor_series_with_magnitude)
    return(sensor_series_with_feat[0], sensor_series_with_feat[1], sensor_series_with_feat[2], sensor_series_with_feat)


        
def lowpass_filter(series, fc = 10, order = 5):
     # fc -> cut-off frequency of the filter, it can't be higher than 25
     w = fc / (fs / 2) # Normalize the frequency
     b, a = signal.butter(order, w, 'low')
     output = signal.filtfilt(b, a, series)
     return(output)


    
def plot(pronation_type, peak_times = None, peak_heights = None,
         ax = False, ay = False, az = False, mag = True, 
         gradient = False, gradient_numpy = False,
         peaks = False):  
    t = np.arange(len(pronation_type)) / fs    
    fig = plt.figure()
    plt.grid(True, 'major')
    if ax == True:
        plt.plot(t, pronation_type[:,2], label = 'Ax')
    if ay == True:
        plt.plot(t, pronation_type[:,3], label = 'Ay')
    if az == True:
        plt.plot(t, pronation_type[:,4], label = 'Az') 
    if mag == True:
        plt.plot(t, pronation_type[:,5], label = 'A (magnitude)')
    if gradient == True:
        plt.plot(t, pronation_type[:,6], label = 'gradient')
    if gradient_numpy == True:
        plt.plot(t, pronation_type[:,7], label = 'gradient')
    if peaks == True:
        plt.plot(peak_times, peak_heights, label = 'peaks')
    plt.legend()
    plt.show(fig)
    
    
    
################################################################################

normal, inverse, everse, pronation_list = load_and_add_features(pronation_type_filenames, my_grad = True)

plot(normal, mag = True)
t = np.arange(len(normal)) / fs
grad_normal = np.gradient(normal[:,5])
mygrad_normal = get_gradient(normal[:,5])
#plt.plot(t, -grad_normal, label = 'np gradient')
plt.plot(t, -mygrad_normal, label = 'my gradient')
plt.legend()

####################### STEP DETECTION AND WINDOWING ####################################

# average recreational runner has 150-170 bpm cadence and we recommend 180. Let's say 200 is max.
# that means that fastest it can get is: a "beat" every 0.3 seconds, but we have one foot only, so 0.6
# our sampling rate is 50hz, thus 0.02s btw each datapoints, thus we don't expect the next peak for another 20 datapoints
# 200 is more of an outlier, max that we recommend in the app is 180 -> 33 datapoints
# the second peak that can cause confustion is close to the first one, so even 30 datapoints should be fine


#plot(normal, mag = True)
#mag_lowpass_10 = lowpass_filter(normal[:,4], 10)
#mag_lowpass_15 = lowpass_filter(normal[:,4], 15)
#mag_lowpass_20 = lowpass_filter(normal[:,4], 20)
#
#t = np.arange(len(normal)) / fs
#plt.plot(t, mag_lowpass_10, label = 'lowpass 10')
#plt.plot(t, mag_lowpass_15, label = 'lowpass 15')
#plt.plot(t, mag_lowpass_20, label = 'lowpass 20')
#plt.legend()

# find peaks
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html

#gradient_accmag_inverse_opposite = -gradient_accmag_inverse
grad_normal_minus = -grad_normal
mygrad_normal_minus = -mygrad_normal
#grad_normal_minus_lp = lowpass_filter(grad_normal_minus, 10, 5)
peaks = signal.find_peaks(mygrad_normal_minus, distance = 20, height = 270, threshold = 200)
# distance = 20, height = 270, threshold = 150 - 279 peaks
# I ended up removing both filter and threshold, because threshold was too stringent and LP useless
# 203 without lowpass
peak_times = peaks[0]/fs
peak_heights = np.array(list(peaks[1]['peak_heights']))

plt.plot(peak_times, peak_heights, 'ro')

time_btw_peaks = np.zeros((len(peaks[0])))
for i in range(0, len(peaks[0])-1):
    time_btw_peaks[i] = (peaks[0][i+1] - peaks[0][i])/fs
     
# separate into steps  
#mean_time_btw_peaks = np.mean(time_btw_peaks)
#sd_time_btw_peaks = np.std(time_btw_peaks)

# let's think about a plausible time for 2 steps (because one foot only)
# 60/165*2 = 0.7272727273
# max: 60/140*2 = 0.86
# min: 60/190*2 = 0.63
    
# if time btw peaks is higher than 0.63 and lower than 0.86, 
# cut at the first bit and the last bit and save as a sample into a list
# then up/down sample each element into one shape... voila
# stack them
# feed them to 

equal_steps = []
labels = []
for j in range (0, len(pronation_list)):
    
    splitting_indices = []
    for i in range(0, len(time_btw_peaks)-1):
        if time_btw_peaks[i] < 0.81 and time_btw_peaks[i] > 0.63:
            splitting_indices.append(peak_times[i])
            splitting_indices.append(peak_times[i+1])
 
    splitting_indices = (np.array(list(splitting_indices))*fs).astype(int)  
    
    # https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.split.html
    # we end up with some zeros, off they go
    sep_steps_list = np.split(normal, splitting_indices)
    sep_steps_list_tidy = []
    sep_steps_length = []
    for i in range(1, len(sep_steps_list)-1):
        if len(sep_steps_list[i]) != 0 and len(sep_steps_list[i]) < 0.81*fs:
            sep_steps_list_tidy.append(sep_steps_list[i])
            sep_steps_length.append(len(sep_steps_list[i]))

    sep_steps_length = np.array(list(sep_steps_length))
    counts = np.bincount(sep_steps_length)
    #most_common_length = np.argmax(counts) # for now it is 35
    most_common_length = 38
    

    for i in range(0, len(sep_steps_list_tidy)):
        if len(sep_steps_list_tidy[i]) != most_common_length:
            # then downsample by:
            # len(step) points - 50 hz
            # 35 points - x hz
            # then, x = 50*35/len_step => x = 46.05 => q = 50/46.0526316 = 1.0857
            # https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.decimate.html#scipy.signal.decimate
            # downsampling factor calculation
            #q = len(sep_steps_list_tidy[i])/most_common_length
            #signal.decimate(sep_steps_list_tidy[i], q, axis = 0)
            
            # https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.resample.html
            fixed_length_step = signal.resample(sep_steps_list_tidy[i], most_common_length)
            equal_steps.append(fixed_length_step)
            
    #    else if len(sep_steps_list_tidy[i]) < most_common_length:
        if len(sep_steps_list_tidy[i]) == most_common_length:
            equal_steps.append(fixed_length_step)
        
        labels.append(j)
# https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.stack.html        

model_input = np.stack(equal_steps, axis = 0)
labels_input = np.array(labels)

#labels = np.full((len(model_input[:,1,1])), 1)



