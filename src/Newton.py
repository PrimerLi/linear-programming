'''
CopyRight 2018
@author Enzhi Li
All rights reserved. 
'''

import numpy as np
import ReadFile
import Gradient
import Hessian

def feasible(A, x, b):
    (row, col) = A.shape
    assert(col == len(x))
    assert(row == len(b))
    slack = A.dot(x) - b
    for i in range(len(slack)):
        if (slack[i] > 0):
            return False
    return True

def invertible(matrix):
    (row, col) = matrix.shape
    assert(row == col)
    inverse = np.linalg.inv(matrix)
    identity = np.diag(np.ones(row))
    eps = 1.0e-10
    return np.linalg.norm(identity - inverse.dot(matrix)) < eps

def newton(t, A, b, c, x0):
    assert(feasible(A, x0, b))
    maxIterationNumber = 20
    eps = 1.0e-8
    count = 0
    while(True):
        count = count + 1
        if (count > maxIterationNumber):
            break
        H = Hessian.Hessian(A, b, x0)
        gradient = Gradient.gradient(t, A, b, c, x0)
        assert(invertible(H))
        inverseOfHessian = np.linalg.inv(H)
        x = x0 - inverseOfHessian.dot(gradient)
        error = np.linalg.norm(x - x0)
        print "count = ", count, ", error = ", error
        x0 = x
        assert(feasible(A, x0, b))
        if (error < eps):
            break
    return x0

def printSolutions(solutions, outputFileName):

    def toString(vector):
        result = ""
        for i in range(len(vector)):
            result = result + str(vector[i]) + "  "
        return result

    ofile = open(outputFileName, "w")
    for i in range(len(solutions)):
        ofile.write(toString(solutions[i]) + "\n")
    ofile.close()

def solver(t0, A, b, c, x0, factor, solutionRecords):
    assert(factor > 1)
    assert(t0 > 0)
    upperBound = 1000*t0
    t = []
    t.append(t0)
    solutions = []
    assert(feasible(A, x0, b))
    solutions.append(x0)
    eps = 1.0e-10
    while(t0 < upperBound):
        solution = newton(t0, A, b, c, x0)
        isFeasible = feasible(A, solution, b)
        if (isFeasible):
            diff = solution - x0
            error = np.linalg.norm(diff)
            solutions.append(solution)
            print solution
            x0 = solution
            t0 = factor*t0
            t.append(t0)
            print "t = ", t0, ", error = ", error
            if (error < eps):
                break
        else:
            break
    printSolutions(solutions, solutionRecords)
    return x0

def main():
    import os
    import sys
    import random

    A, b, c = ReadFile.read("../data/A.txt", "../data/b.txt", "../data/c.txt")
    t = 1.0
    initials = []
    numberOfTests = 4
    for i in range(numberOfTests):
        x0 = np.zeros(len(c))
        for i in range(len(x0)):
            x0[i] = 0.4 + random.uniform(-0.3, 0.3)
        initials.append(x0)
    for i in range(len(initials)):
        print "******************* Test number = "+ str(i + 1) + " **************************"
        factor = 1.2
        solutionRecords = "solutions_" + str(i+1) + ".txt"
        solution = solver(t, A, b, c, initials[i], factor, solutionRecords)
        print "Solution to the problem is: "
        print solution
        print "****************************************************************"
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
