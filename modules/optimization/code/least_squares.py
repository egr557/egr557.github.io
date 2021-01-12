# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:24:11 2020

@author: danaukes
"""

import numpy
import numpy.random
import matplotlib.pyplot as plt
import numpy.linalg
import noisy_data

x,y,y_rand = noisy_data.generate()

ii = 1

A = numpy.array([x,x**2,x**3,numpy.sin(x)]).T

A_inv = numpy.linalg.inv(A.T.dot(A))

coeff = A_inv.dot(A.T.dot(y_rand[:,(ii)]))

y_model = A.dot(coeff)
plt.plot(x,y_rand[:,ii],'.')
plt.plot(x,y_model)

plt.figure()
plt.plot(x,y_model-y_rand[:,ii])
