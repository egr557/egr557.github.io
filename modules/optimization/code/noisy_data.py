# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:40:13 2020

@author: danaukes
"""
import numpy
import matplotlib.pyplot as plt

def generate(x_neg=-10,x_pos = 10,x_step = .1):
    x = numpy.r_[x_neg:x_pos:x_step]
    y1 = x
    y2 = x**2
    y3 = x**3
    y4 = numpy.sin(x)
    
    
    y = numpy.array([y1,y2,y3,y4])
    y = y.T
    y /= y.max(0)
    
    
    rand = numpy.random.randn(*y.shape)
    y_rand = y+rand/10
    return x,y,y_rand

if __name__=='__main__':
    x,y,y_rand = generate()
    plt.plot(x,y)
    plt.plot(x,y_rand,'.')
