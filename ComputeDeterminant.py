import numpy as np


"""
The function below computes determinant of a matrix by Laplace Expansion.

This is an implementation of Algorithm 3.1 from  Gander, et al., Scientific Computing Book
"""

def DetLaplace(A):
    n = A.shape[1]
    if n==1:
        d = A[0,0]
    else:
        d= 0; v = 1
        for j in range(n):
            Temp = np.delete(A,0,0) #Removing the first row from the matrix
            Temp = np.delete(Temp, j, 1) #Removing the jth column from resulting matrix
            d += v * A[0,j] * DetLaplace(Temp)
            v = -v
    
    return d





print(DetLaplace(np.array(((1,0,0, 0),(0,2,0, 0),(0,0,2, 0),(0,0,0,1)))))