"""
Module for finding the intersections of x*cos(pi*x) and 1 - 0.6*x*x 
Modified by: Jeff Wendel
"""
#import numpy as np

from newton import solve
from numpy import pi,cos,sin,linspace
import matplotlib.pyplot as plt

def fvals(x):
    """
    f and f prime for this homework
    """
    #from numpy import pi,cos, sin
    f = (x*cos(pi*x)) - (1. - 0.6*x*x)
    fp = (cos(pi*x) - pi*x*sin(pi*x)) - (-1.2*x)
    return f, fp 


for x0 in [-2.2, -1.5, -0.75, 1.5]:
    print " "  # blank line
    x,iters = solve(fvals, x0, debug=True)
    print "solve returns x = %22.15e after %i iterations " % (x,iters)
    fx,fpx = fvals(x)
    print "the value of f(x) is %22.15e" % fx
    
