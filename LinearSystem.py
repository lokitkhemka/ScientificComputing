import numpy as np

"""
Solves the linear system Ux=b by backsubstitution,
where U is a Upper Triangular matrix (There is no check for U to be Upper Triangular Matrix implemented)
This is an implementation of Algorithm 3.3 from Scientific Computing Book.
"""

def BackSubstitution(U,b):
    n = b.shape[0]
    x = np.zeros(n)
    for k in range(n-1,-1,-1):
        s = b[k]
        for j in range(k+1,n):
            s -= U[k,j] * x[j]
        x[k] = s/U[k,k]
    
    return x


"""
Solves the linear system Ux = b by a variant of Backsubstitution called SAXPY (scalar a.x plus y)
where U is an Upper Triangular Matrix.
This is an implementation of Algorithm 3.4 from Scientific Computing Book.
"""

def BackSubstitutionSAXPY(U,b):
    n = b.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = b[i]/U[i,i]
        b[0:i-1] -= x[i] * U[0:i-1, i]
    return x


print(BackSubstitution(np.array(((1,0,0),(0,1,0), (0,0,1))), np.array(((2),(3),(4)))))
print(BackSubstitutionSAXPY(np.array(((1,0,0),(0,1,0), (0,0,1))), np.array(((2.),(3.),(5.)))))