import numpy as np


def matrix_copy(a: np.array): # Funkcja pozwalająca na utworzenie kopii macierzy
    m = np.zeros((a.shape[0], a.shape[1]), dtype=int)
    for i in range(len(a[0])):
        for j in range(len(a)):
            m[i][j] = a[i][j]
    return m


def deter2(A: np.array):
    det = 0
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return det


def deter(A: np.array):
    det = 0
    det += ((A[0][0] * A[1][1] * A[2][2]) + (A[0][1] * A[1][2] * A[2][0]) + (A[0][2] * A[1][0] * A[2][1])) - (
            (A[0][2] * A[1][1] * A[2][0]) + (A[0][0] * A[1][2] * A[2][1]) + (A[0][1] * A[1][0] * A[2][2])) # Obliczanie wyznacznika metodą Sarrusa.
    return det


def deter4(A: np.array):
    det = 0
    det += A[0][0] * A[1][1] * A[2][2] * A[3][3] + A[0][0] * A[1][2] * A[2][3] * A[3][1] + A[0][0] * A[1][3] * A[2][1] * A[3][2] + A[0][1] * A[1][0] * A[2][3] * A[3][2] + A[0][1] * A[1][2] * A[2][0] * A[3][3] + A[0][1] * A[1][3] * A[2][2] * A[3][0] + A[0][2] * A[1][0] * A[2][1] * A[3][3] + A[0][2] * A[1][1] * A[2][3] * A[3][0] + A[0][2] * A[1][3] * A[2][0] * A[3][1] + A[0][3] * A[1][0] * A[2][2] * A[3][1] + A[0][3] * A[1][1] * A[2][0] * A[3][2] + A[0][3] * A[1][2] * A[2][1] * A[3][0] + - A[0][0] * A[1][1] * A[2][3] * A[3][2] - A[0][0] * A[1][2] * A[2][1] * A[3][3] - A[0][0] * A[1][3] * A[2][2] * A[3][1] + - A[0][1] * A[1][0] * A[2][2] * A[3][3] - A[0][1] * A[1][2] * A[2][3] * A[3][0] - A[0][1] * A[1][3] * A[2][0] * A[3][2] + - A[0][2] * A[1][0] * A[2][3] * A[3][1] - A[0][2] * A[1][1] * A[2][0] * A[3][3] - A[0][2] * A[1][3] * A[2][1] * A[3][0] + - A[0][3] * A[1][0] * A[2][1] * A[3][2] - A[0][3] * A[1][1] * A[2][2] * A[3][0] - A[0][3] * A[1][2] * A[2][0] * A[3][1]
    return det


def rzad(A: np.array):
    if len(A) == 3:
        x = deter(A)
        if x != 0:
            print("Rząd macierzy jest równy 3, bo wyznacznik jest różny od zera")
        else:
            t = matrix_copy(A)
            t_del = np.delete(np.delete(t, 0, 0), 0, 1)
            print(deter2(t_del))
    elif len(A) == 4:
        x = deter4(A)
        if x != 0:
            print("Rząd macierzy jest równy 4, bo wyznacznik jest różny od zera")
        else:
            t = matrix_copy(A)
            t_del = np.delete(np.delete(t, 0, 0), 0, 1)
            print(deter(t_del))
    else:
        print("Podaj inną macierz")


i = np.array([[1, 1, 5], [2, 0, 6], [8, 3, 2]])
j = np.array([[3, -1, 1], [5, 1, 4], [-1, 3, 2]])
y = np.array([[2, 8, 3, -4], [1, 4, 1, -2], [5, 20, 0, -10], [-3, -13, -2, 6]])
x = np.array([[1, 3, -2, 4], [1, -1, 3, 5], [0, 1, 4, -2], [10, -2, 5, 1]])
print("A) ")
rzad(i)
print("B) ")
rzad(j)
print("C) ")
rzad(x)
print("D) ")
rzad(y)


