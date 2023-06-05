from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


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


def manhattan(x_train, i):
    distances = []
    for row in range(len(x_train)):
        current_i = x_train[row]
        current_distance = 0
        for col in range(len(current_i)):
            current_distance += abs(current_i[col] - i[col])
        distances.append(current_distance)
    distances = pd.DataFrame(data=distances, columns=['dist'])
    return distances


def nearest_neighbors(distance_point, k):
    nearest_indices = np.argsort(distance_point['dist'])[:k]
    return distance_point.iloc[nearest_indices]


def predict(nearest, y_train):
    classes = y_train[nearest.index]
    unique_classes, class_counts = np.unique(classes, return_counts=True)
    most_common_class = unique_classes[np.argmax(class_counts)]
    return most_common_class


def knn(k, m , x_test, x_train, y_train=None):
    classes = []
    for i in x_test:
        if m == "euc":
            distance_point = euc(x_train, i)
            nearest = nearest_neighbors(distance_point, k)
            pred = predict(nearest, y_train)
            classes.append(pred)
        if m == "man":
            distance_point = manhattan(x_train, i)
            nearest = nearest_neighbors(distance_point, k)
            pred = predict(nearest, y_train)
            classes.append(pred)
    return classes


xke = knn(3, 'euc', x_test, x_train, y_train)
xk = knn(3, 'man', x_test, x_train, y_train)
print("Wynik funkcji Manhattan: \n", xk)
print("Wynik funkcji Euclides: \n", xke)
kn = KNeighborsClassifier(3)
kn.fit(x_train, y_train)
yk = kn.predict(x_test)
print("Wynik funkcji z sklearn: \n", yk)
print(f'Euclides {accuracy_score(y_test, xke)}')
print(f'Manhattan {accuracy_score(y_test, xk)}')
print(f'Sklearn {accuracy_score(y_test, yk)}')

