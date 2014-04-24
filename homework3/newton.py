
"""
Module for Newton's method for finding the square root of 4.
Modified by: Jeff Wendel
"""


#import numpy as np
#import matplotlib.pyplot as plt

def solve2(fvals, x0, debug=False):

    from numpy import nan
    x=x0    

    if x==0.:
        return 0.
    elif x<0:
        print "*** Error, x must be nonnegative"
        return nan
    assert x>0. and type(x) is float, "Unrecognized input"
        
    s = 1.
    kmax = 100
    tol = 1.e-14
    for k in range(kmax):
        if debug:
            print "Before iteration %s, s = %20.15f" % (k,s)
        s0 = s
        s = 0.5 * (s + x/s)
        delta_s = s - s0
        if abs(delta_s / x) < tol:
            break
    if debug:
        print "After %s iterations, s = %20.15f" % (k+1,s) 
    return s 


def solve(fvals, x0, debug=False):

    from numpy import nan

    maxiter = 20
    tol = 1e-14
    x = 0.
    deltax = 0. 
    fx = 0.
    fxprime = 0.
    k = 0
    
    x=x0    

    if debug:
        print "Initial guess: x = %22.15e" % x0

    kmax = 100
    tol = 1.e-14
    for k in range(maxiter):
        fx, fxprime = fvals(x)
        if abs(fx) < tol:
            break
        deltax = fx/fxprime
        x = x - deltax
        if debug:
            print "After %i iterations, x = %22.15e" % (k+1, x)
    return x, k
    



def fvals_sqrt(x):
    """
    Return f(x) and f'(x) for applying Newton to find a square root.
    """
    f = x**2 - 4.
    fp = 2.*x
    return f, fp

def test1(debug_solve=False):
    """
    Test Newton iteration for the square root with different initial
    conditions.
    """
    from numpy import sqrt
    for x0 in [1., 2., 100.]:
        print " "  # blank line
        x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print "solve returns x = %22.15e after %i iterations " % (x,iters)
        fx,fpx = fvals_sqrt(x)
        print "the value of f(x) is %22.15e" % fx
        assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x
