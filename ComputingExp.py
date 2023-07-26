import numpy as np


"""
Computation of e^x upto a tolerance tol.

This code demonstrates cancellation for large negative x input

Implementation of Algorithm 2.4 from Gander, Gander and Kwok's Scientific Computing Textbook
"""

def ExpUnstable(x, tol):
    s=1; term=1; k=1
    while np.abs(term) > tol*np.abs(s):
        so = s; term =term*x/k
        s = so+term; k+=1
    return s

"""
This function computes exponential function upto the machine precision
It computes e^(abs(x)) and then computes e^(-x) = 1/(e^(abs(x)))

Implementation of Algorithm 2.6 from the textbook
"""

def ExpStable(x):
    if x<0:
        v = -1
        x = np.abs(x)
    else:
        v = 1
    
    so = 0; s = 1; term=1; k = 1
    while s!=so: #This condition becomes true when the total sum doesn't increase due to finite precision of floats
        so = s; term = term*x/k
        s = so+term; k=k+1
    if v<0:
        s = 1/s
    return s

print(ExpUnstable(20, 1.0e-8))
print(np.exp(20))
print(ExpUnstable(1.0, 1.0e-8))
print(np.exp(1))
print(ExpUnstable(-20,1e-8))
print(np.exp(-20))
print("\n")

print(ExpStable(20))
print(np.exp(20))
print(ExpStable(1.0))
print(np.exp(1))
print(ExpStable(-20))
print(np.exp(-20))

