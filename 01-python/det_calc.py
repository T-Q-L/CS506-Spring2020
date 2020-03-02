import numpy as np

def calc(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        print("Matrix is not a square")
        return
    else:
        return round(np.linalg.det(matrix),3)

#matrix = np.array([[1,2],[3,4]])
#print(calc(matrix))