from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier
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


def euc(x_train, i):
    distances = []
    for row in range(len(x_train)):
        current_i = x_train[row]
        current_distance = 0
        for col in range(len(current_i)):
            current_distance += (current_i[col] - i[col]) ** 2
        current_distance = np.sqrt(current_distance)
        distances.append(current_distance)
    distances = pd.DataFrame(data=distances, columns=['dist'])
    return distances


def nearest_neighbors(distance_point, k):
    nearest = distance_point.sort_values(by=['dist'], axis=0)
    nearest = nearest[:k]
    return nearest


def predict(nearest, y_train):
    counter = Counter(y_train[nearest.index])
    classes = counter.most_common()[0][0]
    return classes


def knn(k, m , x_test, x_train, y_train=None):
    classes = []

    for i in x_test:
        if m == "euc":
            distance_point = euc(x_train, i)
            nearest = nearest_neighbors(distance_point, k)
            pred = predict(nearest, y_train)
            classes.append(pred)

    return classes


xk = knn(4, 'euc', x_test, x_train, y_train)
print(xk)
kn = KNeighborsClassifier(4)
kn.fit(x_train, y_train)
yk = kn.predict(x_test)
print(yk)
