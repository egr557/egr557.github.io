# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:28:21 2021

@author: danaukes
"""

#import the pyplot and wavfile modules 

import matplotlib.pyplot as plot

from scipy.io import wavfile
import numpy as np
 

# Read the wav file (mono)

samplingFrequency, signalData = wavfile.read(r'C:\Users\danaukes\Desktop\recording.wav')

signalData = signalData[:,0]

# Plot the signal read from wav file

plot.subplot(211)

plot.title('Spectrogram of a wav file with piano music')

 

plot.plot(signalData)

plot.xlabel('Sample')

plot.ylabel('Amplitude')

 

plot.subplot(212)

powerSpectrum, freqenciesFound, time, imageAxis  = plot.specgram(signalData,Fs=samplingFrequency)

plot.xlabel('Time')

plot.ylabel('Frequency')

 

plot.show()

y = []
for ii in range(len(time)):
    y.append(freqenciesFound[powerSpectrum[:,ii].argmax()])
y = np.array(y)

f = plot.figure()
plot.plot(time,y)