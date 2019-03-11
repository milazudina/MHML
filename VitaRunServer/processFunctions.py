#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:48:06 2019

@author: mila
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from running_frequency import running_frequency
from scipy.stats import zscore

def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / N


def splitter(steps, stepnum, debug=False, log=False, lab1=0, lab2=0):
    stepsnorm = zscore(steps, 0, 0)
    where_are_NaNs = np.isnan(stepsnorm)
    stepsnorm[where_are_NaNs] = 0

    stepsums = np.sum(stepsnorm, axis=1)

    dstepnum = np.diff(stepnum)
    runperiod = np.zeros(dstepnum.shape, dtype=int)

    for i in range(len(dstepnum)):
        if dstepnum[i]: dstepnum[i + 1:i + 20] = 0

    if debug:
        plt.figure()
        for i in range(len(stepsums) - 1):
            if dstepnum[i]: plt.axvline(i - 1, color='r')

    wsize = 128
    wshift = 32
    paces = []

    for i in range(int(((len(steps) - wsize) / wshift))):
        window = steps[i * wshift: i * wshift + wsize - 1, :]
        paces.append(running_frequency(window))
        if paces[-1] > 1.2:
            if debug: plt.axvspan((i) * wshift, (i + 1) * wshift, facecolor='g', alpha=0.3)
            runperiod[i * wshift:(i + 1) * wshift] = 1

    if debug:
        xaxis = np.linspace(0, len(paces) * wshift, len(paces))
        pace = np.asarray(paces, dtype=np.int16)

        plt.plot(stepsums)
        plt.plot(xaxis, pace*100)
        plt.show()

    cutsteps = []

    if log:
        with open("tests.csv", "a", newline='') as f:
            writer = csv.writer(f)

            for i in range(len(stepsums) - 1):
                if runperiod[i] & dstepnum[i]:
                    cutsteps.append(stepsnorm[i:i + 30, :])
                    if debug: writer.writerows(stepsnorm[i:i + 30, :])

        label = []
        nr = 0

        with open("testl.csv", "a", newline='') as f:
            writer = csv.writer(f)

            for i in range(len(stepsums)-1):
                if runperiod[i] & dstepnum[i]:
                    nr+=1
                    for j in range(30):
                        label.append([nr, lab1, lab2])
                        writer.writerow([nr, lab1, lab2])
    else:
        for i in range(len(stepsums) - 1):
            if runperiod[i] & dstepnum[i]:
                cutsteps.append(stepsnorm[i:i + 30, :])

    return(cutsteps)


if __name__ == "__main__":

    filenames = [
        "C:/Mine/ICL/DE4/MHML/Data/ML_data/luka_normal_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/luka_inversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/luka_eversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/timo_normal_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/timo_inversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/timo_eversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/chun_normal_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/chun_inversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/chun_eversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/david_normal_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/david_inversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/david_eversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/keith_normal_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/keith_inversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/keith_eversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/olaf_normal_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/olaf_inversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/olaf_eversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/yann_normal_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/yann_inversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/yann_eversion_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/adi_normal_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/donat_normal_all.csv",
        # "C:/Mine/ICL/DE4/MHML/Data/ML_data/ferg_normal_all.csv"
        ]

    names = [
        [7,1], [7,2], [7,3],
        [8,1], [8,2], [8,3],
        [9,1], [9,2], [9,3],
        [10,1], [10,2], [10,3],
        [11,1], [11,2], [11,3],
        [12,1], [12,2], [12,3],
        [13,1], [13,2], [13,3],
        [14,1], [14,2], [14,3]
        ]

    with open("tests.csv", "w", newline='') as f:
        writer = csv.writer(f)

    with open("testl.csv", "w", newline='') as f:
        writer = csv.writer(f)

    for k in range(len(filenames)):

        stps = []
        accs = []
        stpnr = []
        lab1 = names[k][0]
        lab2 = names[k][1]

        with open(filenames[k], newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(data, None)
            for row in data:
                if row[2][1:5]=="LEFT":
                    stps.append([row[3],row[5],row[6],row[7],row[8],row[9],row[11],row[12],row[13]])
                    stpnr.append(row[17])

        steps = np.asarray(stps, dtype=np.float32)
        stepnum = np.asarray(stpnr, dtype=np.int16)
        splitter(steps[:,:6], stepnum, debug=True, log=True, lab1=0, lab2=0)
        
        
        def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / N


def running_frequency(window):
    windows = np.sum(window, axis=1)
    windowsr = running_mean(windows, 9)

    w = np.fft.fft(windowsr)
    freqs = np.fft.fftfreq(len(w))

    idx = np.argmax(np.abs(w[2:])) + 2
    freq = freqs[idx]
    freq_in_hertz = abs(freq * 50)
    return freq_in_hertz


if __name__ == "__main__": #stand-alone mod for debug

    import csv
    import matplotlib.pyplot as plt

    stps = []
    paces = []

    with open("chun_eversion_all.csv", newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in data:
            stps.append(row)
    steps = np.asarray(stps, dtype=np.float32)

    plt.figure()

    for i in range(int(((len(steps) - 256) / 50))):
        window = steps[i * 50 : i * 50 + 255, :]
        paces.append(running_frequency(window))
        if paces[-1]>1.2: plt.axvspan(i-0.5, i+0.5, facecolor='b', alpha=0.5)

    plt.plot(paces)
    plt.ylabel('Running frequency [Hz]')
    plt.xlabel('Time [s]')
    plt.show()