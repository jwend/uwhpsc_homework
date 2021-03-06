
"""
Demonstration module for polynomial interpolation.
Python module which calculated coefficients for an n degree polynomial for
interpolating and plotting a best fit function for n points
Modified by: Jeff Wendel
"""


import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve

def quad_interp(xi,yi):
    """
    Quadratic interpolation.  Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2.
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2.

    """

    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 3"
    assert len(xi)==3 and len(yi)==3, error_message

    # Set up linear system to interpolate through data points:
    ### Fill in this part to compute c ###
    A = np.vstack([np.ones(3), xi, xi**2]).T
    
    b = yi

    # Solve the system:
    c = solve(A,b)

    #print "The polynomial coefficients are:"
    #print c

    return c


def plot_quad(xi, yi):

    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 3"
    assert len(xi)==3 and len(yi)==3, error_message
     
    c = quad_interp(xi,yi)
    
    # Plot the resulting polynomial:
    #x = np.linspace(-2,3,1001)   # points to evaluate polynomial
    x = np.linspace(xi.min() - 1,  xi.max() + 1, 1000)
    y = c[0] + c[1]*x + c[2]*x**2

    plt.figure(1)       # open plot figure window
    plt.clf()           # clear figure
    plt.plot(x,y,'b-')  # connect points with a blue line

    # Add data points  (polynomial should go through these points!)
    plt.plot(xi,yi,'ro')   # plot as red circles
    plt.ylim(-20,20)         # set limits in y for plot

    plt.title("Data points and interpolating polynomial")

    plt.savefig('quadratic.png')   # save figure as .png file


def cubic_interp(xi,yi):
    """
    Cubic interpolation.  Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2,3.
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2 +c[3]*pow(x,3)

    """

    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 4"
    assert len(xi)==4 and len(yi)==4, error_message

    # Set up linear system to interpolate through data points:
    ### Fill in this part to compute c ###
    A = np.vstack([np.ones(4), xi, xi**2, pow(xi,3)]).T
    
    b = yi

    # Solve the system:
    c = solve(A,b)

    #print "The polynomial coefficients are:"
    #print c

    return c


def plot_cubic(xi, yi):

    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 4"
    assert len(xi)==4 and len(yi)==4, error_message
     
    c = cubic_interp(xi,yi)
    
    # Plot the resulting polynomial:
    #x = np.linspace(-2,3,1001)   # points to evaluate polynomial
    x = np.linspace(xi.min() - 1,  xi.max() + 1, 1000)
    y = c[0] + c[1]*x + c[2]*x**2 + c[3]*pow(x,3)

    plt.figure(1)       # open plot figure window
    plt.clf()           # clear figure
    plt.plot(x,y,'b-')  # connect points with a blue line

    # Add data points  (polynomial should go through these points!)
    plt.plot(xi,yi,'ro')   # plot as red circles
    plt.ylim(-20,20)         # set limits in y for plot

    plt.title("Data points and interpolating polynomial")

    plt.savefig('cubic.png')   # save figure as .png file




def poly_interp(xi,yi):
    """
    Generalized polynomial interpolation.  
    Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,...,n.
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2 +c[3]*pow(x,3)... + c[n-1]*pow(x,n-1)

    """

    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have equal length"
    assert len(xi) == len(yi), error_message

    # Set up linear system to interpolate through data points:
    ### Fill in this part to compute c ###
    A = np.ndarray(shape=(len(xi),len(yi)))
    for i in range(0,len(xi)):
        for j in range(0,len(yi)):
            A[i][j] = pow(xi[j],i)
    A=A.T
#    print A
    
    b = yi

    # Solve the system:
    c = solve(A,b)
    return c


def plot_poly(xi, yi):

    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have equal length"
    assert len(xi)== len(yi), error_message
     
    c = poly_interp(xi,yi)
#    print c 
#    print len(c)
    # Plot the resulting polynomial:
    #x = np.linspace(-2,3,1001)   # points to evaluate polynomial
    x = np.linspace(xi.min() - 1,  xi.max() + 1, 1000)
    y = np.zeros(len(x))
    #y = c[0] + c[1]*x + c[2]*x**2 + c[3]*pow(x,3)
#    for i in range(0,len(x)):
#        y[i]=0
#        for m in range(0,len(c)):
#            y[i] = y[i] + c[m]*pow(x[i],m)
#        print x[i], y[i]
    n=len(c)        
    y = c[n-1]
    for j in range(n-1, 0, -1):
        y = y*x + c[j-1]

    plt.figure(1)       # open plot figure window
    plt.clf()           # clear figure
    plt.plot(x,y,'b-')  # connect points with a blue line

    # Add data points  (polynomial should go through these points!)
    plt.plot(xi,yi,'ro')   # plot as red circles
    plt.ylim(-20,20)         # set limits in y for plot

    plt.title("Data points and interpolating polynomial")

    plt.savefig('poly.png')   # save figure as .png file


def test_quad1():
    """
    Test code, no return value or exception if test runs properly.
    """
    xi = np.array([-1.,  0.,  2.])
    yi = np.array([ 1., -1.,  7.])
    c = quad_interp(xi,yi)
    c_true = np.array([-1.,  0.,  2.])
    print "c =      ", c
    print "c_true = ", c_true
    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)

def test_quad2():
    """
    Test code, no return value or exception if test runs properly.
    """
    xi = np.array([-3.,  -1.,  2.])
    yi = np.array([ 10., -9.,  7.])
    c = quad_interp(xi,yi)
    #c_true = np.array([-1.,  0.,  2.])
    c_true = np.array([-9.6, 2.36666667, 2.96666667])
    print "c =      ", c
    print "c_true = ", c_true
    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)


def test_cubic1():
    """
    Test code, no return value or exception if test runs properly.
    """
    xi = np.array([-3., -1.,  2.,  5.])
    yi = np.array([ 10.,  -9.,   7.,  11.])
    c = cubic_interp(xi,yi)
    c_true = np.array([-6.875, 4.6375,2.05833333, -0.45416667])
    print "c =      ", c
    print "c_true = ", c_true
    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)

def test_poly1():
    """
    Test code, no return value or exception if test runs properly.
    """
    xi = np.array([-3., -1.,  2.,  5.])
    yi = np.array([ 10.,  -9.,   7.,  11.])
    c = poly_interp(xi,yi)
    c_true = np.array([-6.875, 4.6375,2.05833333, -0.45416667])
    print "c =      ", c
    print "c_true = ", c_true
    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)


def test_poly2():
    """
    Test code, no return value or exception if test runs properly.
    """
    xi = np.array([-3., -1.,  2.,  5., 7.])
    yi = np.array([ 10.,  -9.,   7.,  11., -3.])
    c = poly_interp(xi,yi)
    c_true = np.array([-5.8875,5.26291667,1.56458333,-0.55291667,0.03291667])
    print "c =      ", c
    print "c_true = ", c_true
    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)



        
if __name__=="__main__":
    # "main program"
    # the code below is executed only if the module is executed at the command line,
    #    $ python demo2.py
    # or run from within Python, e.g. in IPython with
    #    In[ ]:  run demo2
    # not if the module is imported.
    print "Running test..."
    test_quad1()
    test_quad2()
    test_cubic1()
    test_poly1()
    test_poly2()

