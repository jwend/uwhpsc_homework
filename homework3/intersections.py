"""
Module for finding the intersections of x*cos(pi*x) and 1 - 0.6*x*x 
Modified by: Jeff Wendel
"""
#import numpy as np

from newton import solve
from numpy import pi,cos,sin,linspace,array
import matplotlib.pyplot as plt


def fvals(x):
    """
    f and f prime for this homework
    """
    #from numpy import pi,cos, sin
    f = (x*cos(pi*x)) - (1. - 0.6*x*x)
    fp = (cos(pi*x) - pi*x*sin(pi*x)) - (-1.2*x)
    return f, fp 

xlist =[]
for x0 in [-2.2, -1.5, -0.75, 1.5]:
    print " "  # blank line
    x,iters = solve(fvals, x0, debug=True)
    xlist.append(x)
    print "solve returns x = %22.15e after %i iterations " % (x,iters)
    fx,fpx = fvals(x)
    print "the value of f(x) is %22.15e" % fx

x0s = array(xlist)    
x1 =  linspace(-5., 5., 1000)
f1 = x1*cos(pi*x1) 
g1 = 1. - 0.6*x1*x1

plt.figure(1)       # open plot figure window
plt.clf()           # clear figure
plt.plot(x1,f1,'r-')  # connect points with a blue line
plt.plot(x1,g1,'b-')  # connect points with a blue line
# add intersections
y0s = x0s * cos(pi*x0s)
plt.plot(x0s,y0s,'ko')   # plot as black circles
plt.title("Intersections")
plt.savefig('intersections.png')   # save figure as .png file
