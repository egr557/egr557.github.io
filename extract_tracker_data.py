# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:54:15 2021

@author: danaukes
"""

import pandas as pd
import numpy
import matplotlib.pyplot as plt
import scipy.interpolate as si

df=pd.read_csv(r'C:\Users\danaukes\Documents\Tracker\mydata.csv', sep=',')

#x = df.x.astype('float64').to_numpy()
x = df.x.to_numpy()
y = df.y.to_numpy()
t = df.t.to_numpy()


xy = numpy.array([x,y]).T
f = si.interp1d(t,xy.T,fill_value='extrapolate',kind='quadratic')
new_t = numpy.r_[0:t[-1]:.1]

plt.figure()
plt.plot(t,x)
plt.plot(new_t,f(new_t)[0])

plt.figure()
plt.plot(t,y)
plt.plot(new_t,f(new_t)[1])
plt.figure()
plt.plot(x,y)

