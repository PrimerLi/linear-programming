import ReadFile
import numpy as np

def Hessian(A, b, x):
    (row, col) = A.shape
    m = len(b) # number of constraints
    n = len(x) # number of variables
    assert(m == row)
    assert(n == col)
    slack = A.dot(x) - b
    vector = np.zeros(len(slack))
    for i in range(len(vector)):
        vector[i] = 1.0/(slack[i]**2)
    D = np.diag(vector)
    return A.transpose().dot(D).dot(A)

def main():
    import os
    import sys

    A, b, c = ReadFile.read("../data/A.txt", "../data/b.txt", "../data/c.txt")
    x = np.zeros(len(c))
    x[0] = 0.1
    x[1] = 0.2
    H = Hessian(A, b, x)
    ReadFile.printMatrix(H)
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
