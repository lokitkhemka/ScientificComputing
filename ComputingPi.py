import numpy as np
from decimal import Decimal


"""
This is an implementation of Algorithm 2.1 from Gander, Gander and Kwok Scientific Computing Textbook.
This code demonstrates the effects of the cancellation (when subtracting floating point numbers that are really close) in floating point numbers.
THIS CODE IS NOT MEANT FOR PRODUCTION USE.
"""
def ComputingPiNaive():
    s = np.sqrt(3)/2; A = 3*s; n=6 #A is the area of the polygon of n sides with side length of 1. For large n, A = pi
    output = [[n, A, A-np.pi]]
    while (s>1e-10):
        s = np.sqrt((1-np.sqrt(1-s*s))/2)
        n=2*n; A = n/2 * s
        output.append([n,A, A-np.pi])
    for i in range(len(output)):
        print(f"{output[i][0]}, {output[i][1]}, {output[i][2]}, \n")

"""
The function below is the implementation of Algorithm 2.2 from Gander, Gander and Kwok Scientific Computing book.
This code provides the solution to the cancellation as demonstrated in the function "ComputingPiNaive" above.
Also, the loop termination is independent of the machine precision as the loop terminates,
when newA is not longer greater than oldA.
"""
def ComputingPiStable():
    oldA = 0; s = np.sqrt(3)/2; newA = 3*s; n=6 #oldA and newA is the area of the polygon of n sides with side length of 1. For large n, newA = pi
    output = [[n, newA, newA-np.pi]]
    while (newA > oldA):
        oldA = newA
        s = s/np.sqrt(2*(1+np.sqrt((1+s) * (1-s))))
        n= 2*n; newA = n/2 * s
        output.append([n, newA, newA-np.pi])
    for i in range(len(output)):
        print(f"{output[i][0]}, {output[i][1]}, {output[i][2]}, \n")


# ComputingPiNaive()
ComputingPiStable()