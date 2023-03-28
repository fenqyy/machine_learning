import numpy as np


def matrix_jedn(a: np.array):
    x = matrix_copy(a)
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j:
                x[i][j] = 1
            else:
                x[i][j] = 0
    return x


def matrix_copy(a: np.array):
    m = np.zeros((a.shape[0], a.shape[1]), dtype=int)
    for i in range(len(a[0])):
        for j in range(len(a)):
            m[i][j] = a[i][j]
    return m


def multiplication(A: np.array, B: np.array) -> np.array:
    result = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]).reshape(3,
                                                                 3)  # Pusta macierz. Będzie przechoywać wynik mnożenia.
    if A.shape[1] == B.shape[0]:  # Sprawdzenie czy mnożenie macierzy jest możliwe.
        for i in range(len(A)):  # Pętla po wierszach macierzy A.
            for j in range(len(B[0])):  # Pętla po kolumnach macierzy B.
                for k in range(len(B)):  # Pętla po wierszach macierzy B.
                    result[i][j] += A[i][k] * B[k][j]  # Do pustej macierzy dodajemy wynik mnożenia.
    else:
        print("Nie można pomnożyć tych macierzy.")  # Jeżeli mnożenie nie jest możliwe, wyświetla komunikat.
    return result


def odw(x: np.array):
    mj = matrix_jedn(x)
    mjc = matrix_copy(mj)
    xc = matrix_copy(x).astype(dtype=float)
    dlug = len(xc)
    for i in range(dlug):
        wartosc = 1 / xc[i][i].astype(dtype=float)
        for j in range(dlug):
            xc[i][j] *= wartosc
        indexes = list(range(dlug))

    print(xc)


x = np.array([[8, 1, 4, 2, 1], [8, 6, 4, 2, 1], [1, 2, 3, 4, 1], [8, 0, 6, 2, 5], [1, 9, 6, 4, 1]])
print(matrix_jedn(x))
