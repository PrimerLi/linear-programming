import ReadFile
import numpy as np

def gradient(t, A, b, c, variables):
    numberOfVariables = len(variables)
    n = len(c)
    m = len(b)
    (row, col) = A.shape
    assert(row == m) # number of constraints
    assert(col == n) # number of variables
    assert(numberOfVariables == n)

    slack = A.dot(variables) - b
    vector = np.zeros(m)
    for i in range(m):
        vector[i] = 1.0/slack[i]
    g = t*c - A.transpose().dot(vector)
    return g

def main():
    import os
    import sys
    
    A, b, c = ReadFile.read("../data/A.txt", "../data/b.txt", "../data/c.txt")
    x = np.zeros(len(c))
    x[0] = 0.1
    x[1] = 0.2
    t = 1.0
    print "Gradient = ", gradient(t, A, b, c, x)
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
