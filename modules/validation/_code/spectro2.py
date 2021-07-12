# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:39:20 2021

@author: danaukes
"""

# import the libraries

import matplotlib.pyplot as plot

import numpy as np

 

# Define the list of frequencies

frequencies         = np.arange(5,105,5)

 

# Sampling Frequency

samplingFrequency   = 400

 

# Create two ndarrays

s1 = np.empty([0]) # For samples

s2 = np.empty([0]) # For signal

 

# Start Value of the sample

start   = 1

 

# Stop Value of the sample

stop    = samplingFrequency+1

 

for frequency in frequencies:

    sub1 = np.arange(start, stop, 1)

 

    # Signal - Sine wave with varying frequency + Noise

    sub2 = np.sin(2*np.pi*sub1*frequency*1/samplingFrequency)
    # sub2 += +np.random.randn(len(sub1))

  

    s1      = np.append(s1, sub1)

    s2      = np.append(s2, sub2)

   

    start   = stop+1

    stop    = start+samplingFrequency

 

# Plot the signal

plot.subplot(211)

plot.plot(s1,s2)

plot.xlabel('Sample')

plot.ylabel('Amplitude')

 

 

# Plot the spectrogram

plot.subplot(212)

powerSpectrum, freqenciesFound, time, imageAxis = plot.specgram(s2, Fs=samplingFrequency)

plot.xlabel('Time')

plot.ylabel('Frequency')

 

plot.show()   


y = []
for ii in range(len(time)):
    y.append(freqenciesFound[powerSpectrum[:,ii].argmax()])
y = np.array(y)

f = plot.figure()
plot.plot(time,y)