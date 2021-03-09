# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:29:01 2020

@author: danaukes
"""

import cma
import numpy
import matplotlib.pyplot as plt
import scipy.optimize
import numpy.random

def plot_params(parameters):
    A,b,w,w0 = parameters
    f = A*numpy.sin(w*t-w0)+b
    p = ax.plot(t,f)
    return p

t = numpy.r_[0:10:.1]
fig = plt.figure()
ax = fig.add_subplot()

parameters = (10,2,2.1,3.3)
ini = [1]*len(parameters)

A,b,w,w0 = parameters
f0 = A*numpy.sin(w*t-w0)+b
f0 += numpy.random.randn(*t.shape)*10/10
p1=ax.plot(t,f0,'.')

def myfunc(parameters):
    A,b,w,w0 = parameters
    f1 = A*numpy.sin(w*t-w0)+b
    error = ((f1-f0)**2).sum()
    return error

sol = scipy.optimize.minimize(myfunc,ini)
p2 = plot_params(sol.x)

es = cma.CMAEvolutionStrategy(ini, 0.5)
# annotate the print of disp
es.logger.disp_header()
# Iterat Nfevals  function value    axis ratio maxstd  minstd
while not es.stop():
      X = es.ask()
      es.tell(X, [myfunc(x) for x in X])
      # log current iteration
      es.logger.add()
      # display info for last iteration   #doctest: +ELLIPSIS
      es.logger.disp([-1])
es.logger.disp_header()
# Iterat Nfevals  function value    axis ratio maxstd  minstd
# will make a plot
# es.logger.plot()
p3 = plot_params(es.best.x)

plt.legend([p1[0],p2[0],p3[0]],['data','minimize()','CMA-ES'])
