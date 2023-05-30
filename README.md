# KNN

# Importowane są niezbędne biblioteki: sklearn.datasets do wczytania zbioru danych Iris, numpy do operacji numerycznych, pandas do manipulacji danymi,
# Counter z modułu collections do zliczania wystąpień, KNeighborsClassifier z sklearn.neighbors do klasyfikacji KNN z użyciem biblioteki scikit-learn.
# Za pomocą load_iris() wczytywany jest zbiór danych Iris. Wczytywane są cechy (x) oraz etykiety (y) dla każdego przykładu.
# Następuje podział danych na zbiór treningowy (70% danych) i zbiór testowy (30%) za pomocą train_test_split() z sklearn.model_selection.
# Funkcja euc() oblicza odległość Euklidesową między punktami w zbiorze treningowym x_train a pojedynczym punktem i. Przechodzi przez każdy wiersz w zbiorze treningowym
# i oblicza odległość dla każdej cechy. Wyniki są zapisywane w ramce danych distances i zwracane jako wynik funkcji.
# Funkcja nearest_neighbors() sortuje wyniki odległości punktu distance_point i wybiera k najbliższych sąsiadów. Następnie zwraca te najbliższe sąsiadki.
# Funkcja predict() prognozuje klasę na podstawie najbliższych sąsiadów. Wykorzystuje obiekt Counter do zliczania wystąpień klas w y_train dla indeksów najbliższych sąsiadów.
# Zwraca klasę, która występuje najczęściej.
# Funkcja knn() implementuje algorytm KNN dla zestawu testowego. Iteruje przez każdy punkt w x_test.
# Jeśli metryka jest ustawiona na "euc" (odległość Euklidesowa), oblicza odległości między x_train a tym punktem testowym, a następnie znajduje k najbliższych sąsiadów.
# Na podstawie tych sąsiadów przewiduje klasę za pomocą funkcji predict() i dodaje wynik do listy klas.
# Na koniec, wynik klasyfikacji z funkcji knn() jest wydrukowany (xk).
# Następnie tworzony jest obiekt KNeighborsClassifier o k=4 sąsiadach.
# Przygotowuje się model klasyfikatora na zbiorze treningowym za pomocą fit(). Przewiduje klasy dla zbioru testowego za pomocą predict() i wynik jest drukowany (yk).
# Podsumowując, kod ten implementuje KNN za pomocą dwóch różnych metod - niestandardowej implementacji (knn) oraz wbudowanej klasyfikatora KNN z biblioteki scikit-learn (KNeighborsClassifier).
# Porównuje wyniki tych dwóch implementacji dla zbioru danych Iris.
