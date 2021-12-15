import numpy as np
import scipy.signal
from matplotlib import pyplot as plt

from Soundboard import *

def unmake(name):
    wav_file = wave.open(name + ".wav")
    nframes = wav_file.getnframes() * 16
    frames = wav_file.readframes(nframes)
    ticks = 0
    percent = -1
    string = ""
    for i in range(0,nframes,2):
        try:
            string += str(struct.unpack('h',bytes(frames[i-2:i]))[0])+"\n"
        except:
            pass
        ticks += 2
        if percent < math.floor(ticks / nframes * 100):
            percent = math.floor(ticks / nframes * 100)
            print("\rUncompiling: " + str(percent) + "%", end="")
    wav_file.close()
    build = open(name + ".txt", "w")
    build.write(string)
    build.close()

def plot(name):
    file = open(name + ".txt", "r")
    signal = []
    N = filesize(name + ".txt")
    for i in range(N):
        signal.append(file.readline()[:-1])

def spectrum(name):
    file = open(name+".txt","r")
    signal = []
    N = filesize(name + ".txt")
    for i in range(N):
        signal.append(int(file.readline()[:-1])/DRANGE)
    return scipy.signal.spectrogram(np.array(signal), SAMPLERATE, nfft=2^16)

def spectrogram(name):
    file = open(name + ".txt", "r")
    signal = []
    N = filesize(name + ".txt")
    for i in range(N):
        signal.append(int(file.readline()[:-1]) / DRANGE)
    f, t, Sxx = scipy.signal.spectrogram(np.array(signal), SAMPLERATE, nfft=4096)
    plt.pcolormesh(t, f[0:80], Sxx[0:80])
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()
