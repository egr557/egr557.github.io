# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:24:11 2020

@author: danaukes
"""

import numpy
import numpy.random
import matplotlib.pyplot as plt
import numpy.linalg
import scipy.optimize

import noisy_data 

x,y,y_rand = noisy_data.generate()

ii=2

A = numpy.array([(x),(x)**2,(x)**3,numpy.sin(x)]).T



def myfunc(coeffs):
    coeffs = numpy.array(coeffs)

    # print(coeffs)
    y_model = (coeffs[None,:]*A).sum(1)
    
    # print(y_model.shape)
    error = ((y_model-y_rand[:,ii])**2).sum()
    
    return error



sol = scipy.optimize.minimize(myfunc,[1]*A.shape[1])

y_model = (sol.x[None,:]*A).sum(1)


# plt.figure()
plt.plot(x,y_rand[:,ii],'.')
plt.plot(x,y_model)
