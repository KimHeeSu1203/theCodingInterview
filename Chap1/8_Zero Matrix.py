import unittest
import copy
import random

def findZeroMatrix(rows, cols, matrix, rowZero, colZero):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                rowZero.append(i)
                colZero.append(j)

    return rowZero,colZero

def makeZeroMatrixRow(rowZero, cols, matrix_du):
    for i in rowZero:
        for j in range(cols):
            matrix_du[i][j] = 0
    return matrix_du

def makeZeroMatrixCol(rows,colZero, matrix_du):
    for i in range(rows):
        for j in colZero:
            matrix_du[i][j] =0
    return matrix_du


rows = 5
cols = 4
matrix = [[random.randint(0,10) for _ in range(cols)] for _ in range(rows)]

matrix_du = copy.deepcopy(matrix)
rowZero = []
colZero = []

rowZero,colZero = findZeroMatrix(rows, cols, matrix, rowZero, colZero)
print("row", rowZero)
print("col", colZero)
matrix_du = makeZeroMatrixRow(rowZero, cols, matrix_du)
matrix_du = makeZeroMatrixCol(rows,colZero, matrix_du)
for i in range(len(matrix)):
    print(matrix[i])

print("")
for i in range(len(matrix)):
    print(matrix_du[i])