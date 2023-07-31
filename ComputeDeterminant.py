import numpy as np


"""
The function below computes determinant of a matrix by Laplace Expansion.

This is an implementation of Algorithm 3.1 from  Gander, et al., Scientific Computing Book

Returns None for Non-square matrices
"""

def DetLaplace(A):
    n = A.shape[1]
    if (A.shape[0] == A.shape[1]):
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
    return None


"""
The function Cramer solves Ax=b, where A is a square matrix and b is the column matrix.

It uses the function `DetLaplace` from above to compute determinants.

This is an implementation of algorithm 3.2 from Gander et al., Scientific Computing Book
Returns None for non-square A matrix
Returns x as a Row Matrix
"""

def Cramer(A,b):
    n = b.shape[0]
    if (A.shape[0] == A.shape[1] == b.shape[0]):
        detA = DetLaplace(A)
        x = np.zeros(n)
        for i in range(n):
            Temp = np.delete(A,i, 1)
            AI = np.insert(Temp,i,b, 1)
            x[i] = DetLaplace(AI)/detA
        return x
    else:
        return None



print(DetLaplace(np.array(((1,0,0, 0),(0,2,0, 0),(0,0,2, 0),(0,0,0,1)))))
print(DetLaplace(np.array(((1,0,0, 0),(0,2,0, 0),(0,0,2, 0)))))

print(Cramer(np.array(((1,0,0),(0,1,0), (0,0,1))), np.array(((2),(3),(4)))))