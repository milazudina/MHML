import numpy as np


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