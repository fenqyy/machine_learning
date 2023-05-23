from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# W poniższym kodzie najpierw importujemy load_iris z sklearn.datasets, a następnie wczytujemy dane przy użyciu iris = load_iris().
# cechy zawierają cechy irysów, a klasy zawierają etykiety klas. Następnie stosujemy funkcję train_test_split, podając cechy i klasy jako argumenty,
# aby podzielić je na zbiory treningowe i testowe.
# Parametr test_size określa, jaką część danych chcemy przypisać do zbioru testowego (w tym przypadku 0.3 oznacza 30% danych testowych).
#
# Na koniec wyświetlamy podział na zbiór treningowy i testowy, aby sprawdzić wyniki.


iris = load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
print("Zbiór treningowy (cechy):", x_train)
print("Zbiór treningowy (klasy):", y_train)
print("Zbiór testowy (cechy):", x_test)
print("Zbiór testowy (klasy):", y_test)


def KNN(k, x_test, x_train, y_train=None):
    classes = []

    for i in x_test:

