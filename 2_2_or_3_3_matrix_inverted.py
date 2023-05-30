import numpy as np


def deter(A: np.array):
    det = 0
    det += ((A[0][0] * A[1][1] * A[2][2]) + (A[0][1] * A[1][2] * A[2][0]) + (A[0][2] * A[1][0] * A[2][1])) - (
            (A[0][2] * A[1][1] * A[2][0]) + (A[0][0] * A[1][2] * A[2][1]) + (A[0][1] * A[1][0] * A[2][2])) # Obliczanie wyznacznika metodą Sarrusa.
    return det


def transport(A: np.array):
    tab = np.zeros((A.shape[1], A.shape[0]),
                   dtype=np.uint8)  # Pusta tablica wypełniona zerami o wymiarach macierzy podanej jako argument.
    for i in range(len(A[0])):  # Pętla po kolumnach macierzy A.
        for j in range(len(A)):  # Pętla po wierszach macierzy A.
            tab[i, j] = A[j, i]  # Przypisanie odwrotnej wartości do pustej tablicy.
    return tab


def odw2_2(A: np.array):
    B = np.array([[0, 0], [0, 0]])
    C = np.array([[0, 0], [0, 0]], dtype=np.uint8)
    D = np.array([[0, 0], [0, 0]], dtype=float)
    deter = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    print("Wyznacznik macierzy wynosi: ", deter)
    if deter > 0:
        B[0][0] = A[1][1]
        B[0][1] = -1 * A[1][0]
        B[1][0] = -1 * A[0][1]
        B[1][1] = A[0][0]
        print("\nMacierz dopełnień algebraicznych: \n", B)
        C = transport(B)
        print("\nMacierz dopełnień algebraicznych po transponowaniu: \n", C)
        D[0][0] = C[0][0] / deter
        D[0][1] = C[0][1] / deter
        D[1][0] = C[1][0] / deter
        D[1][1] = C[1][1] / deter
        print("\nMacierz odwrotna: \n", D)
    else:
        print("Macierz nieosobliwa.")


def odw3_3(A: np.array):
    tab = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=float)
    x = deter(A)
    print("Wyznacznik macierzy: ", x)
    if x != 0:
        tab[0][0] = (1 / x) * ((A[1][1] * A[2][2]) - (A[1][2] * A[2][1]))
        tab[0][1] = (1 / x) * ((A[0][2] * A[2][1]) - (A[0][1] * A[2][2]))
        tab[0][2] = (1 / x) * ((A[0][1] * A[1][2]) - (A[0][2] * A[1][1]))
        tab[1][0] = (1 / x) * ((A[1][2] * A[2][0]) - (A[1][0] * A[2][2]))
        tab[1][1] = (1 / x) * ((A[0][0] * A[2][2]) - (A[0][2] * A[2][0]))
        tab[1][2] = (1 / x) * ((A[0][2] * A[1][0]) - (A[0][0] * A[1][2]))
        tab[2][0] = (1 / x) * ((A[1][0] * A[2][1]) - (A[1][1] * A[2][0]))
        tab[2][1] = (1 / x) * ((A[0][1] * A[2][0]) - (A[0][0] * A[2][1]))
        tab[2][2] = (1 / x) * ((A[0][0] * A[1][1]) - (A[0][1] * A[1][0]))
    else:
        print("Macierz nieosobliwa.")
    return tab

X = np.array([[3, 6], [0, 9]])
Y = np.array([[-3, -9], [1, 3]])
Z = np.array([[1, 0, 5], [2, 7, 6], [8, 3, 2]])
S = np.array([[3, -1, 1], [5, 1, 4], [-1, 3, 2]])
# odw2_2(X)
# odw2_2(Y)
print(odw3_3(Z))
print(np.linalg.inv(Z))
