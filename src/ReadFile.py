import numpy as np

def readMatrix(inputFileName):
    import os
    assert(os.path.exists(inputFileName))
    ifile = open(inputFileName, "r")
    string = ifile.readline()
    a = string.split()
    row = int(a[0])
    col = int(a[1])
    A = np.zeros((row, col))
    for i in range(row):
        string = ifile.readline()
        a = string.split()
        for j in range(len(a)):
            A[i, j] = float(a[j])
    ifile.close()
    return A

def readVector(inputFileName):
    import os
    assert(os.path.exists(inputFileName))
    ifile = open(inputFileName, "r")
    line = ifile.readline().strip()
    length = int(line)
    vector = np.zeros(length)
    for i in range(length):
        line = ifile.readline().strip()
        vector[i] = float(line)
    ifile.close()
    return vector

def printMatrix(matrix):
    (row, col) = matrix.shape
    for i in range(row):
        for j in range(col):
            print matrix[i, j], "  ", 
        print "\n", 

def read(AFile, bFile, cFile):
    import os

    assert(os.path.exists(AFile))
    assert(os.path.exists(bFile))
    assert(os.path.exists(cFile))

    A = readMatrix(AFile)
    b = readVector(bFile)
    c = readVector(cFile)
   
    if (False):
        print "c = ", c
        print "A = "
        printMatrix(A)
        print "b = ", b

    return A, b, c

def main():
    A, b, c = read("../data/A.txt", "../data/b.txt", "../data/c.txt")
    if (True):
        print "c = ", c
        print "A = "
        printMatrix(A)
        print "b = ", b

if __name__ == "__main__":
    import sys
    sys.exit(main())
