import numpy as np


def multiplication(A: np.array, B: np.array) -> np.array:
    result = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]).reshape(3, 3)
    if A.shape[1] == B.shape[0]:
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][i]
    else:
        print("Nie można pomnożyć tych macierzy.")
    return result

def determinant_3x3(A: np.array):



A = np.array([[2, 1, 1], [1, 3, 6], [4, 5, 5]]).reshape(3, 3)
B = np.array([[1, 0, 5], [2, 1, 6], [0, 3, 0]]).reshape(3, 3)
C = np.array([[1, 4, 5], [2, 1, 6], [0, 3, 2]]).reshape(3, 3)
print(multiplication(A, B))
